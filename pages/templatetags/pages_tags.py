from django import template
from pages.models import Page

register = template.Library()

@register.inclusion_tag('pages/page_object.html', takes_context=True)
def render_page(context, slug, *args, **kwargs):
    request = context['view'].request

    try:
        if getattr(Page.objects, "platform", False):
            query = Page.objects.platform(request.platform).get(
                enabled=True,
                slug=slug
                )
        else:
            query = Page.objects.get(
                enabled=True,
                slug=slug
                )
    except Page.DoesNotExist, Page.MultipleObjectsReturned:
        query = None

    context["page"] = query
    return context