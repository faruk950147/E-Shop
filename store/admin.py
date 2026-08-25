from django.contrib import admin
from store.models import (
    Category
)

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = (
        'id', 'parent', 'title', 'slug', 'additional', 'description', 'image_tag', 'is_featured',
        'status', 'created_at', 'updated_at'
    )
    
    list_editable = ('is_featured', 'status')

    search_fields = ('title', 'additional', 'description')

    list_filter = ('status', 'is_featured')

    readonly_fields = ('created_at','updated_at','image_tag')

    fieldsets = (
        (None, {
            "fields": (
                'parent', 'title', 'slug', 'additional', 'description', 'image', 
                'is_featured', 'status',
            ),
        }),
    )
    class Media:
        js = (
            "http://ajax.googleapis.com/ajax/google/code-js/jquery.min.js",
            "http://ajax.googleapis.com/ajax/google/code-js/jquery-ui.min.js",
            "modeltranslation/js/tabbed_translation_fields.js",
        )
        css = {
            "screen": ("modeltranslation/css/tabbed_translation_fields.css",),
        }


