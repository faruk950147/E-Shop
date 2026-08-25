from django.db import models
from decimal import Decimal
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    EmailValidator,
)

User = get_user_model()

from common.common import (
    BaseMixin, CommonMixin 
)

from mixins.mixins import (
    LoginRequiredMixin, ImageTagMixin, StripMixin, ColorTagMixin 
)
from validation.validators import (
    validate_image_size, validate_file_extension
)


# ======================== CATEGORY ========================
class Category(StripMixin, BaseMixin, CommonMixin, ImageTagMixin):
    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="children",
    )
    title = models.CharField(_("title"), max_length=255, unique=True)
    image = models.ImageField(
        _("image"),
        upload_to="categories/%Y/%m/%d/",
        validators=[validate_image_size, validate_file_extension],
        default="defaults/default.jpg",
    )
    is_featured = models.BooleanField(_("is_featured"), default=False)

    class Meta:
        verbose_name_plural = "01. Categories"
        db_table = "store_categories"
        ordering = ["id"]

        # Composite or single-field indexing for frequently queried fields
        indexes = [
            models.Index(fields=["is_featured", "status"]),
            models.Index(fields=["created_at"]),
            models.Index(fields=["updated_at"]),
        ]

    def clean(self):
        super().clean()

        # 1. Prevent self-parenting
        if self.parent_id and self.pk and self.parent_id == self.pk:
            raise ValidationError(_("A category cannot be its own parent."))

        # 2. Strict 3-level depth check (Root -> Child -> Sub-child)
        depth = 0
        curr = self.parent
        while curr is not None:
            depth += 1
            if depth >= 3:
                raise ValidationError( _("Maximum nesting level (3 levels) reached."))
            if curr.pk == self.pk:
                raise ValidationError(_("Circular hierarchy detected."))
            curr = curr.parent

    def __str__(self):
        return self.title