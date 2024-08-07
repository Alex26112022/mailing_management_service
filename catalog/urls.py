from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from catalog.apps import CatalogConfig
from catalog.views import ProductCreateView, \
    ProductListView, ContactlistView, ProductDetailView, ProductUpdateView, \
    ProductDeleteView, CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', ContactlistView.as_view(), name='contacts'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()),
         name='get_product'),
    path('add_product/', never_cache(ProductCreateView.as_view()),
         name='add_product'),
    path('update_product/<int:pk>/', never_cache(ProductUpdateView.as_view()),
         name='update_product'),
    path('delete_product/<int:pk>/', never_cache(ProductDeleteView.as_view()),
         name='delete_product'),
    path('category/', CategoryListView.as_view(), name='category')
]
