from .models import SiteName, Logo, Footer

def site_settings(request):
    """
    Injects site configuration singletons globally into template contexts.
    """
    return {
        'site_name': SiteName.objects.filter(status='active').first(),
        'site_logo': Logo.objects.filter(status='active').first(),
        'site_footer': Footer.objects.filter(status='active').prefetch_related('links').first(),
    }