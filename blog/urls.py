from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogDetailView, BlogCreateView, \
    BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='index'),
    path('add_blog/', BlogCreateView.as_view(), name='add_blog'),
    path('<slug:slug>/', BlogDetailView.as_view(), name='detail'),
    path('edit_blog/<slug:slug>/', BlogUpdateView.as_view(), name='edit_blog'),
    path('delete_blog/<slug:slug>/', BlogDeleteView.as_view(),
         name='delete_blog'),  # noqa
]
