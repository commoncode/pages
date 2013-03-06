from django.contrib import admin
from pages import models as page_models

try:
    # Only import from platforms if it is a dependancy
    from platforms import settings as platforms_settings
    if platforms_settings.USE_PLATFORMS:
        from platforms import admin as platforms_admin
        # Use platform mixin if platforms is found as a dependancy
        PlatformObjectInline = [platforms_admin.PlatformObjectInline]
    else:
        raise ImportError
except ImportError:
    PlatformObjectInline = []


class PageAdmin(admin.ModelAdmin):    
    actions_on_top = True

    list_display = ('title', 'slug',)
    search_fields = ('title', 'slug',)

    prepopulated_fields = {
        "slug": ("title",)
    }

    inlines = PlatformObjectInline

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