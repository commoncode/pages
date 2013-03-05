from django.db import models
from entropy.base import SlugMixin, TitleMixin, TextMixin

try:
    # Only import from platforms if it is a dependancy
    from platforms import models as platforms_models
    # Use platform mixin if platforms is found as a dependancy
    ObjectManager = platforms_models.PlatformObjectManager
except ImportError:
    ObjectManager = models.Manager


class Page(SlugMixin, TitleMixin, TextMixin):

    objects = ObjectManager()