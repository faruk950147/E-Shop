from django.conf import settings


def settings_context(request):
    return {
        "SITE_NAME": "E-Shop",
        "SUPPORTED_LANGUAGES": settings.LANGUAGES,
    }