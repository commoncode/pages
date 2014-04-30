from cqrs.serializers import CQRSSerializer

from .models import Page


class PageSerializer(CQRSSerializer):
    class Meta:
        model = Page
        fields = (
            'id',
            'title',
            'slug',
            'text',
            'created_at',
            'featured'
        )
