from django.contrib import admin
from setting.models import Footer, Link


class BaseAdmin(admin.ModelAdmin):
    """
    Base Admin class providing common configuration for models inheriting from BaseMixin.
    """
    list_display = ("id", "status", "created_at", "updated_at")
    list_editable = ("status",)
    search_fields = ()
    list_filter = ("status", "created_at", "updated_at")
    ordering = ("-id",)
    list_per_page = 25
    date_hierarchy = "created_at"
    readonly_fields = ("created_at", "updated_at")


class SingletonAdmin(BaseAdmin):
    """
    Enforces a single object instance for settings models in the admin.
    """
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False


class LinkInline(admin.TabularInline):
    """
    Inline admin for managing Links directly within the Footer.
    """
    model = Link
    extra = 1
    fields = ("title", "url", "status")
    show_change_link = True


@admin.register(Footer)
class FooterAdmin(SingletonAdmin):
    list_display = (
        "id", "copyright_text", "phone", "email", "status", "updated_at",
    )
    search_fields = ("about_text", "address", "phone", "email")
    inlines = [LinkInline]