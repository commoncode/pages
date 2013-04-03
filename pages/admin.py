from django.contrib import admin
from entropy.admin import InlineAttributeAdmin
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


class PageSetting(InlineAttributeAdmin):
    verbose_name = "Page Setting"
    verbose_name_plural = verbose_name + 's'


class PageAdmin(admin.ModelAdmin):    
    actions_on_top = True

    list_display = ('title', 'slug', 'enabled',)
    search_fields = ('title', 'slug',)
    list_filter = ('enabled',)
    list_editable = ( 'enabled',)

    prepopulated_fields = {
        "slug": ("title",)
    }

    inlines = [
        PageSetting
    ] + PlatformObjectInline

    fieldsets = (
        (None, {
            'fields': (
                'enabled', 'featured', 'publishing_status', 'published_date',
            )
        }),
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