from setting.models import Logo

def site_settings(request):
    """
    Inject active site configuration into all template contexts.
    """

    return {
        "site_logo": Logo.objects.filter(
            status="active"
        ).first(),
    }