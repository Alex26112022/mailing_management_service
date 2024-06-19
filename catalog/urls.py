from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductCreateView, \
    ProductListView, ContactlistView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', ContactlistView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='get_product'),
    path('add_product/', ProductCreateView.as_view(), name='add_product')
]
