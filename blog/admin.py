from django.contrib import admin
from django.utils.safestring import mark_safe

from blog.models import Blog


@admin.register(Blog)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'created_at', 'is_published', 'views_count')
    list_filter = ('is_published',)
    search_fields = ('title',)
    list_display_links = ('pk', 'title', 'created_at', 'is_published', 'views_count')
    fields = ['title', 'content', 'photo', 'preview', 'is_published']
    readonly_fields = ['preview']

    def preview(self, obj):
        return mark_safe(
            f'<img src="{obj.photo.url}" style="max-height: 200px;">')
