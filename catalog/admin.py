from django.contrib import admin

from catalog.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('title', 'description')
    list_display_links = ('pk', 'title', 'price', 'category')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
    list_display_links = ('pk', 'title')
