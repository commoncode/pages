from django.core.management.base import BaseCommand

from ...factories import PageFactory


class Command(BaseCommand):
    help = 'Create Categories and add products'

    def handle(self, *args, **options):
        for i in range(10):
            page = PageFactory()

            print 'Page: {}'.format(page.title)
