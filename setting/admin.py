from django.contrib import admin
from setting.models import Logo


@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "image_tag", "status", "created_at", "updated_at")
    list_display_links = ("id", "title")
    list_filter = ("status", "created_at", "updated_at")
    search_fields = ("title",)
    readonly_fields = ("image_tag", "created_at", "updated_at")

    fieldsets = (
        (None,
            {"fields": ("title", "image", "image_tag", "status", "created_at", "updated_at"),},
        ),
    )
