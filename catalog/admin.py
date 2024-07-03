from django.contrib import admin
from django.utils.safestring import mark_safe

from catalog.models import Product, Category, Contacts, Version


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('title', 'description')
    list_display_links = ('pk', 'title', 'price', 'category')
    fields = ['title', 'description', 'image', 'preview', 'price', 'category']
    readonly_fields = ['preview']

    def preview(self, obj):
        return mark_safe(
            f'<img src="{obj.image.url}" style="max-height: 200px;">')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
    list_display_links = ('pk', 'title')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product', 'version', 'title', 'current_version')
    list_display_links = (
        'pk', 'product', 'version', 'title', 'current_version')
    ordering = ('product',)
    list_filter = ('product',)


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'address', 'phone')
    list_display_links = ('pk', 'title', 'address', 'phone')
