from django.contrib import admin
from setting.models import Logo, Footer, Link


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



@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "phone", "copyright_text", "status", "created_at", "updated_at")
    list_display_links = ("id", "email")
    list_filter = ("status", "created_at", "updated_at")
    search_fields = ("about_text", "address", "phone", "email", "copyright_text")
    readonly_fields = ("created_at", "updated_at")
    
    fieldsets = (
        (None, {
            "fields": ("email", "phone", "copyright_text", "status"),
        }),
    )


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "url", "status", "created_at", "updated_at")
    list_display_links = ("id", "title")
    list_filter = ("status", "created_at", "updated_at")
    search_fields = ("title", "url")
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        (None, {
            "fields": ("title", "url", "status"),
        }),
    )