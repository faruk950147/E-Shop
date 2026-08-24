from django.contrib import admin
from setting.models import Footer, Link


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "phone", "copyright_text", "status", "created_at" "updated_at")
    list_display_links = ("id", "email")
    list_filter = ("status", "created_at", "updated_at")
    search_fields = ("about_text", "address", "phone", "email", "copyright_text")
    readonly_fields = ("created_at", "updated_at")
    
    add_fieldsets = (
        ("email", "phone", "copyright_text", "status")
    )

    fieldsets = (
        ("email", "phone", "copyright_text", "status")
    )


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "url", "status", "created_at" "updated_at")
    list_display_links = ("id", "title")
    list_filter = ("status", "created_at", "updated_at")
    search_fields = ("title", "url")
    readonly_fields = ("created_at", "updated_at")

    add_fieldsets = (
        ("title", "url", "status")
    )

    fieldsets = (
        ("title", "url", "status")
    )