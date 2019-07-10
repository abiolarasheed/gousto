# coding: utf-8
from rest_framework import serializers
from recipe.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """
    This class represents the response for recipe lookup
    """

    class Meta:
        model = Recipe
        fields = "__all__"


class CuisineSerializer(serializers.ModelSerializer):
    """
    This class represents the response for cuisine lookup
    """

    description = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = ("id", "title", "description")

    @staticmethod
    def get_description(obj: Recipe) -> str:
        """
        This helper method transforms `marketing_description` to description
        key in the CuisineSerializer
        """
        return obj.marketing_description
