from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogDetailView, BlogCreateView, \
    BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='index'),
    path('<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('add_blog/', BlogCreateView.as_view(), name='add_blog'),
    path('edit_blog/<int:pk>/', BlogUpdateView.as_view(), name='edit_blog'),
    path('delete_blog/<int:pk>/', BlogDeleteView.as_view(), name='delete_blog'),  # noqa
]
