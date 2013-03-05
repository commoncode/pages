from django.db import models

from entropy.base import SlugMixin, TitleMixin, TextMixin


try:
    # Only import from platforms if it is a dependancy
    from platforms import models as platforms_models
    # Use platform mixin if platforms is found as a dependancy
    PlatformObjectManagerMixin = platforms_models.PlatformObjectManagerMixin
except ImportError:
    PlatformObjectManagerMixin = object


class Page(SlugMixin, TitleMixin, TextMixin, PlatformObjectManagerMixin):
    pass