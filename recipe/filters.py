from django_filters.rest_framework import CharFilter, FilterSet

from recipe.models import Recipe


class RecipeFilter(FilterSet):
    cuisine = CharFilter(field_name="recipe_cuisine", lookup_expr="icontains")

    class Meta:
        model = Recipe
        fields = ["cuisine"]
