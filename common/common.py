from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


# STATUS
STATUS_CHOICES = (
    ("active", _("Active")),
    ("inactive", _("Inactive")),
)

# VARIANT TYPE
VARIANT_TYPE_CHOICES = (
    ("none", _("None")),
    ("color", _("Color")),
    ("size", _("Size")),
    ("color_size", _("Color Size")),
)


# SLIDER TYPE
SLIDER_TYPE_CHOICES = (
    ("none", _("None")),
    ("slider", _("Slider")),
    ("add", _("Add")),
    ("feature", _("Feature")),
    ("promotion", _("Promotion")),
)


STATUS_CHOICES = (
    ("active", _("Active")),
    ("inactive", _("Inactive")),
)

# BASE MIXIN
class BaseMixin(models.Model):
    status = models.CharField(_("Status"), max_length=20, choices=STATUS_CHOICES, default="active")
    created_at = models.DateTimeField(_("Created_at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated_at"), auto_now=True)

    class Meta:
        abstract = True


# COMMON MIXIN
class CommonMixin(models.Model):
    slug = models.SlugField(_("Slug"), max_length=255, unique=True, blank=True, null=True)
    additional = models.CharField(_("Additional"), max_length=255, blank=True, null=True)
    description = models.CharField(_("Description"), max_length=255, blank=True, null=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            # Parent model-এর title field
            if hasattr(self, "title"):
                base_slug = slugify(self.title)
            else:
                base_slug = slugify(str(self))

            self.slug = base_slug

        super().save(*args, **kwargs)