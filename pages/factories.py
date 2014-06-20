import factory

from django.contrib.webdesign.lorem_ipsum import paragraphs, words
from django.template.defaultfilters import slugify

from faker import Factory


fake = Factory.create()


class PageFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'pages.Page'
    FACTORY_DJANGO_GET_OR_CREATE = ('title', 'slug')

    title = factory.LazyAttribute(lambda o: words(2, common=False).title())
    text = factory.LazyAttribute(lambda o: paragraphs(3, common=False))
    slug = factory.LazyAttribute(lambda o: slugify(o.title))
