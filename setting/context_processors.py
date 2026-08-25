from setting.models import Logo, Footer


def site_settings(request):
    """
    Inject active site configuration into all template contexts.
    """

    return {
        "site_logo": Logo.objects.filter(
            status="active"
        ).first(),

        "site_footer": Footer.objects.filter(
            status="active"
        ).prefetch_related("links").first(),
    }