from django.urls import path, include

from recipe.router import router


urlpatterns = [path("api/", include(router.urls))]
