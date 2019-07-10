from typing import Union, Dict, Any

from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from recipe.filters import RecipeFilter
from recipe.models import Recipe
from recipe.pagination import DefaultResultsSetPagination
from recipe.serializers import RecipeSerializer, CuisineSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    """
    This class implements main API Allow-Methods: [GET, PUT, PATCH, DELETE, HEAD, OPTIONS]
    """

    queryset = Recipe.objects.all().order_by("id")
    filterset_class = RecipeFilter
    pagination_class = DefaultResultsSetPagination

    def partial_update(
        self, request: Request, *args: Any, **kwargs: Dict[str, Any]
    ) -> Response:
        kwargs["partial"] = True
        self.update(request, *args, **kwargs)
        return Response(request.data)

    def get_serializer_class(self) -> Union[RecipeSerializer, CuisineSerializer]:
        """
        Dynamically select serializer_class
        """
        if self.request.GET.get("cuisine", None) is None:
            return RecipeSerializer
        return CuisineSerializer
