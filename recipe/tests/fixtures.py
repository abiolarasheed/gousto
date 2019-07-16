# coding: utf-8
from random import choice
from typing import Union, List

from django.db.models import QuerySet
from mixer.backend.django import mixer
import pytest
from rest_framework.test import APIRequestFactory
from recipe.models import Recipe


@pytest.fixture(scope="function")
def factory() -> APIRequestFactory:
    """ Creates a request object. """
    request = APIRequestFactory()
    return request


@pytest.fixture(scope="function")
def recipe(db) -> Recipe:
    """ Creates a recipe object. """
    recipe = mixer.blend(Recipe)
    return recipe


@pytest.fixture(scope="function")
def recipes(db) -> Union[QuerySet, List[Recipe]]:
    """ Creates a recipe QuerySet. """
    cuisines = ("asian", "british", "mexican", "italian")
    recipes = mixer.cycle(25).blend(
        Recipe, recipe_cuisine=(choice(cuisines) for _ in range(25))
    )
    return recipes
