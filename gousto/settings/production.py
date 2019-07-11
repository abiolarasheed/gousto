from .base import *

DEBUG=False
ALLOWED_HOSTS = ["*"]  # This just so you can run this app now we. We will need change in real production environment.


REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",)

}
