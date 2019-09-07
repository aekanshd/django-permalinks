from django.contrib import admin
from django.utils.html import format_html

from .models import Permalinks


class PermalinksAdmin(admin.ModelAdmin):
    """Admin options for Permalinks"""
    change_form_template = 'admin/url_shortner_script.html'

    fieldsets = [
        ('URL Redirects', {
            'fields': [
                'old_url',
                'new_url',
            ],
        }),
    ]

    list_display = (
        'old_url',
        'new_url',
    )

    search_fields = [
        'old_url',
        'new_url',
    ]


admin.site.register(Permalinks, PermalinksAdmin)