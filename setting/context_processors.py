from setting.models import Footer, Link

def settings_context(request):
    """
    Context processor to pass active Footer and Link data to all templates.
    """
    footer = Footer.objects.filter(status="active").prefetch_related("links").first()

    return {
        'footer': footer,
    }