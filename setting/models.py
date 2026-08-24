from django.db import models
from django.utils.translation import gettext_lazy as _

from common.common import (
    BaseMixin,
    StripMixin
)


class Footer(StripMixin, BaseMixin):
    about_text = models.TextField(
        _("about_text"),
        blank=True,
        null=True,
        help_text=_("Short description about the company"),
    )
    address = models.CharField(
        _("address"),
        max_length=255,
        blank=True,
        null=True,
    )
    phone = models.CharField(
        _("phone"),
        max_length=50,
        blank=True,
        null=True,
    )
    email = models.EmailField(
        _("email"),
        blank=True,
        null=True,
    )
    # Copyright
    copyright_text = models.CharField(
        _("copyright_text"),
        max_length=255,
        default="All rights reserved",
        help_text=_("Custom copyright notice line"),
    )
    class Meta:
        verbose_name_plural = "01. Footer"
        db_table = "settings_footer"
        ordering = ["id"]
        
        # indexing for faster queries
        indexes = [
            models.Index(fields=["status"]),
            models.Index(fields=["created_at"]),
            models.Index(fields=["updated_at"]),
        ]


class Link(StripMixin, BaseMixin):
    title = models.CharField(
        _("Title"),
        max_length=100,
        help_text=_("e.g. Quick Links, Legal, Policies"),
    )
    url = models.URLField(
        _("url"),
        help_text=_("Display order of column headers"),
    )

    class Meta:
        verbose_name_plural = "02. Link"
        db_table = "settings_link"
        ordering = ["id"]
        
        # indexing for faster queries
        indexes = [
            models.Index(fields=["status"]),
            models.Index(fields=["created_at"]),
            models.Index(fields=["updated_at"]),
        ]


    def __str__(self):
        return self.title


