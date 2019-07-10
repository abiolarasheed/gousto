from .base import *

SECRET_KEY = "$%v(0lm%)r@*g83mm#9v0-_5aaorlu^s+6d%g7%=zh51p_qya9"

REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

PASSWORD_HASHERS = ("django.contrib.auth.hashers.MD5PasswordHasher",)
LOGGING = {}
