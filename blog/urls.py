from django.urls import path

from blog.apps import BlogConfig
from blog.views import blog_index

app_name = BlogConfig.name

urlpatterns = [
    path('', blog_index, name='index'),
]
