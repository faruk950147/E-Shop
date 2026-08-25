from store.models import Category
from django.utils import translation

def store_context(request):
    """Context processor to make store categories globally available in templates."""
    # 1. Get current language from request (e.g., 'en', 'bn')
    user_language = getattr(request, 'LANGUAGE_CODE', 'en')
    
    # 2. Activate language context for this request thread
    translation.activate(user_language)

    # 3. Return queryset standardly (MultilingualQuerySet will pick up the active language)
    return {
        "categories": Category.objects.filter(parent__isnull=True)
    }