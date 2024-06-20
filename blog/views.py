from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, CreateView,
                                  UpdateView, DeleteView, \
                                  )
from pytils.translit import slugify

from blog.models import Blog


class BlogListView(ListView):
    """ Выводит список всех постов блога. """
    model = Blog
    paginate_by = 4

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    """ Выводит один пост блога. """
    model = Blog


class BlogCreateView(CreateView):
    """ Создает новый пост блога. """
    model = Blog
    fields = ('title', 'content', 'photo')
    success_url = reverse_lazy('blog:index')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    """ Редактирует пост блога. """
    model = Blog
    fields = ('title', 'content', 'photo')
    success_url = reverse_lazy('blog:index')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)


class BlogDeleteView(DeleteView):
    """ Удаляет пост блога.  """
    model = Blog
    success_url = reverse_lazy('blog:index')
