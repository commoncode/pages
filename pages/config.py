from django.apps import AppConfig
from django.utils.importlib import import_module


class PageConfig(AppConfig):
    name = 'pages'
    verbose_name = 'Pages'

    def ready(self):
        import_module('pages.collections')
