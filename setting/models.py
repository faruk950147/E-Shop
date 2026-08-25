from django.db import models
from django.utils.translation import gettext_lazy as _

from common.common import BaseMixin, SingletonMixin
from mixins.mixins import StripMixin, ImageTagMixin
from validation.validators import validate_image_size, validate_file_extension



class Logo(StripMixin, SingletonMixin, BaseMixin, ImageTagMixin):
    title = models.CharField(_('title'), unique=True, max_length=150, help_text='Site Logo')
    image = models.ImageField(
        _("image"),
        upload_to="logo/%Y/%m/%d/",
        validators=[validate_image_size, validate_file_extension],
        default="defaults/default.jpg",
    )

    class Meta:
        verbose_name = _("Logo")
        verbose_name_plural = _("02. Logo")
        db_table = "settings_logo"

    def __str__(self):
        return self.title
    
    
    
    