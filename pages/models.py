from django.db import models
from django.core.urlresolvers import reverse
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

    def get_absolute_url(self):
        """Returns the absolute url for a single page instance
        """
        return reverse('pages_detail_page', args=(self.slug,))

    @staticmethod
    def get_list_url():
        """Returns the absolute url for all page objects. This is a
           static method.
        """
        return reverse('pages_all_pages')
