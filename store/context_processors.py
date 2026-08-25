from store.models import Category  # Adjust the import path to match your app structure


def store_context(request):
    """Context processor to make store categories globally available in templates."""
    return {
        # Prefetch child categories to optimize queries for your dropdown menus
        "categories": Category.objects.filter(parent=None).prefetch_related(
            "children"
        )
    }