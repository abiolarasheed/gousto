# coding: utf-8
from random import choice, randrange
from typing import Union, List

from django.db.models import QuerySet
from mixer.backend.django import mixer
import pytest
from rest_framework.reverse import reverse
from rest_framework.test import APIRequestFactory

from recipe.api import RecipeViewSet
from recipe.models import Recipe


@pytest.fixture()
def factory() -> APIRequestFactory:
    request = APIRequestFactory()
    return request


@pytest.fixture()
def recipe(db) -> Recipe:
    recipe = mixer.blend(Recipe)
    return recipe


@pytest.fixture()
def recipes(db) -> Recipe:
    cuisines = ("asian", "british", "mexican", "italian")
    recipes = mixer.cycle(25).blend(
        Recipe, recipe_cuisine=(choice(cuisines) for _ in range(25))
    )
    return recipes


def test_recipe_detail_view(recipe: Recipe, factory: APIRequestFactory) -> None:
    """Test API client can see a recipe's details"""
    # build url
    url = reverse("recipe-detail", args=(recipe.pk,))

    # Create request object
    request = factory.get(url, format="json")

    # Make request to api view
    view = RecipeViewSet.as_view(actions={"get": "retrieve"})
    response = view(request, pk=recipe.pk)

    # Test if request was successful
    assert response.status_code == 200


def test_recipe_list(
    factory: APIRequestFactory, recipes: Union[QuerySet, List[Recipe]]
) -> None:
    """ Test that Api client can get list of paginated recipe"""
    # build urls
    url = reverse("recipe-list")
    page2 = f"http://testserver{url}?page=2"

    # Create request object
    request = factory.get(url)

    # Make request to api view
    view = RecipeViewSet.as_view(actions={"get": "list"})
    response = view(request)

    assert response.status_code == 200

    # Test we have 10 results per page
    assert len(response.data.get("results", [])) == 10

    # Just checking if there is even a page 2
    assert response.data.get("next") == page2

    # Get all the fields in the models
    recipe_fields = sorted([f.name for f in Recipe._meta.get_fields()])

    # Test that we get full recipe fields for every recipe
    recipe_json = response.data.get("results")[randrange(10)]
    assert sorted(recipe_json.keys()) == recipe_fields


def test_recipe_by_cuisine(
    factory: APIRequestFactory, recipes: Union[QuerySet, List[Recipe]]
) -> None:
    """Test that each recipe has to contain only the fields ID, title and description"""
    # build urls
    cuisine = recipes[0].recipe_cuisine
    path = reverse("recipe-list")

    url = "{}?cuisine={}".format(path, cuisine)

    # Create request object
    request = factory.get(url)

    # Make request to api view
    view = RecipeViewSet.as_view(actions={"get": "list"})
    response = view(request)

    assert response.status_code == 200

    # Test each recipe has to contain only the fields ID, title and description
    cuisine_fields = ["description", "id", "title"]
    # get all the fields in the models

    # test that we get full recipe fields for every recipe
    recipe_json = response.data.get("results")[0]
    assert sorted(recipe_json.keys()) == cuisine_fields


def test_partial_update(factory: APIRequestFactory, recipe: Recipe) -> None:
    """
    Test API client can update one or more recipe's fields
    """

    # Test data
    data = {"title": "Sausages With Potato Salad & Caramelised Onion"}

    # build url
    url = reverse("recipe-detail", args=(recipe.pk,))

    # Create request object
    request = factory.patch(url, data, format="json")

    # Make request to api view
    view = RecipeViewSet.as_view(actions={"patch": "partial_update"})
    response = view(request, pk=recipe.pk)

    old_title = recipe.title
    recipe.refresh_from_db()  # Pull latest update from database after update

    # Test if request was successful
    assert response.status_code == 200

    # Test updated field are returned
    assert response.data == data

    # Test recipe title was updated
    assert old_title != recipe.title
