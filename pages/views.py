from django.views.generic import DetailView, ListView

from .models import Page

try:
    # Only import from platforms if it is a dependancy
    from platforms import views as platforms_views
    # Use platform mixin if platforms is found as a dependancy
    PlatformListMixin = platforms_views.PlatformListMixin
    PlatformDetailMixin = platforms_views.PlatformDetailMixin
except ImportError:
    PlatformDetailMixin = PlatformListMixin = object


class AllPages(PlatformListMixin, ListView):
    model=Page
    template_name = "pages/page_list.html"


def all_pages(request):
    return AllPages.as_view()(request)


class DetailPage(PlatformDetailMixin, DetailView):
    model = Page
    template_name = "pages/page_detail.html"


def detail(request, slug):
    return DetailPage.as_view()(request, slug=slug)