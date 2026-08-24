from django.db import models
from django.utils.translation import gettext_lazy as _

from common.common import (
    BaseMixin,
    StripMixin
)

from django.db import models
from django.utils.translation import gettext_lazy as _


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
        indexes = [
            models.Index(fields=["status"]),
            models.Index(fields=["created_at"]),
            models.Index(fields=["updated_at"]),
        ]


class Link(StripMixin, BaseMixin):
    footer = models.ForeignKey(
        Footer,
        on_delete=models.CASCADE,
        related_name="links",
    )
    title = models.CharField(
        _("title"),
        max_length=100,
        help_text=_("e.g. Quick Links, Legal, Policies"),
    )
    url = models.URLField(
        _("url"),
        help_text=_("Target URL for this link"),
    )

    class Meta:
        verbose_name_plural = "02. Links"
        db_table = "settings_link"
        ordering = ["id"]
        indexes = [
            models.Index(fields=["status"]),
            models.Index(fields=["created_at"]),
            models.Index(fields=["updated_at"]),
        ]

    def __str__(self):
        return f"{self.title} ({self.url})"