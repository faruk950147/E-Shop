from store.models import (
    Category
)


def store_context(request):
    return {
        "categories": Category.objects.filter(status="active")
    }