from recipe.api import RecipeViewSet

from rest_framework import routers

router = routers.DefaultRouter()

router.register("recipe", RecipeViewSet)
