from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, contacts, get_product, ProductCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', get_product, name='get_product'),
    path('add_product/', ProductCreateView.as_view(), name='add_product')
]
