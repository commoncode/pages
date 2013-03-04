from django.db import models

from entropy.base import SlugMixin, TitleMixin, TextMixin


class Page(SlugMixin, TitleMixin, TextMixin):
    pass