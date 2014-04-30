from cqrs.mongo import mongodb
from cqrs.collections import DRFDocumentCollection

from .models import Page
from .serializers import PageSerializer


class PageDocumentCollection(DRFDocumentCollection):
    model = Page
    serializer_class = PageSerializer
    name = 'economica__pages'


mongodb.register(PageDocumentCollection())
