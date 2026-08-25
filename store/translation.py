
from modeltranslation.translator import TranslationOptions, register

from store.models import (
    Category
)


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('parent', 'title', 'slug', 'additional', 'description', 'image', 'is_featured', 'status') 