from django.contrib import admin
from pages import models as page_models

try:
    # Only import from platforms if it is a dependancy
    from platforms import admin as platforms_admin
    # Use platform mixin if platforms is found as a dependancy
    PlatformInlineMixin = platforms_admin.PlatformInlineMixin
except ImportError:
    PlatformInlineMixin = object()


class PageAdmin(PlatformInlineMixin, admin.ModelAdmin):
    actions_on_top = True

    list_display = ('title', 'slug',)
    search_fields = ('title', 'slug',)

    prepopulated_fields = {
        "slug": ("title",)
    }

    fieldsets = (
        # (None, {
        #     'fields': (
        #         'enabled',
        #     )
        # }),
        ("Content", {
            'fields': [
                'title',
                'short_title',
                'slug',
                'text',
            ]
        }),
    )


admin.site.register(page_models.Page, PageAdmin)