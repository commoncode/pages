from django.core.management.base import BaseCommand

from ...models import Page


class Command(BaseCommand):
    help = 'Clean up Menus'

    def handle(self, *args, **options):
        Page.objects.all().delete()
