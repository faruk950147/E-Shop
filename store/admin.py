from django.contrib import admin
from store.models import (
    Category
)

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = (
        'id', 'parent', 'title', 'slug', 'keyword', 'description', 'image_tag', 'is_featured',
        'status', 'created_at', 'updated_at'
    )
    
    list_editable = ('is_featured', 'status')

    search_fields = ('title', 'keyword', 'description')

    list_filter = ('status', 'is_featured')

    readonly_fields = ('created_at','updated_at','image_tag')
    
    add_fieldsets = (
        (None, {
            "fields": (
                'parent', 'title', 'slug', 'keyword', 'description', 'image', 
                'is_featured', 'status',
            ),
        }),
    )

    fieldsets = (
        (None, {
            "fields": (
                'parent', 'title', 'slug', 'keyword', 'description', 'image', 
                'is_featured', 'status',
            ),
        }),
    )
