from django.apps import AppConfig
from django.utils.importlib import import_module


class PagesConfig(AppConfig):
    name = 'pages'
    verbose_name = 'Pages'

    def ready(self):
        import_module('pages.collections')
