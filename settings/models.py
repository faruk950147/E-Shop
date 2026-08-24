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

