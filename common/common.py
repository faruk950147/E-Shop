from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


# STATUS
class StatusChoices(models.TextChoices):
    Active = "active", _("Active")
    Inactive = "inactive", _("Inactive")


# VARIANT TYPE 
class VariantType(models.TextChoices):
    NONE = "none", _("None")
    COLOR = "color", _("Color")
    SIZE = "size", _("Size")
    COLOR_SIZE = "color_size", _("Color Size")


# SLIDER TYPE
class SliderType(models.TextChoices):
    NONE = "none", _("None")
    SLIDER = "slider", _("Slider")
    ADD = "add", _("Add")
    FEATURE = "feature", _("Feature")
    PROMOTION = "promotion", _("Promotion")


# BASE MIXIN 
class BaseMixin(models.Model):
    status = models.CharField(
        _("Status"),
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.Active,
    )
    created_at = models.DateTimeField(_("Created_at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated_at"), auto_now=True)

    class Meta:
        abstract = True


# COMMON MIXIN
class CommonMixin(models.Model):
    slug = models.SlugField(_("Slug"), max_length=255, unique=True, blank=True, null=True)
    keyword = models.CharField(_("Keyword"), max_length=255, blank=True, null=True)
    description = models.CharField(_("Description"), max_length=255, blank=True, null=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            # title field parent model 
            if hasattr(self, "title"):
                base_slug = slugify(self.title)
            else:
                base_slug = slugify(str(self))

            self.slug = base_slug

        super().save(*args, **kwargs)
        
