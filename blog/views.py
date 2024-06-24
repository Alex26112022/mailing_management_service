from django.shortcuts import render  # noqa
from django.urls import reverse_lazy, reverse
from django.views.generic import (ListView, DetailView, CreateView,
                                  UpdateView, DeleteView)
from pytils.translit import slugify

from blog.models import Blog
from blog.send_yandex_mail import send_yandex_mail


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

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save()
        max_views_count = 100
        if obj.views_count >= max_views_count:
            yandex_message = (f'<a href="http://127.0.0.1:8000/blog/'
                              f'{obj.slug}/">{obj.title}</a>')
            send_yandex_mail(yandex_message, max_views_count)
            print('Проверьте почту!!!')
        return obj


class BlogCreateView(CreateView):
    """ Создает новый пост блога. """
    model = Blog
    fields = ('title', 'content', 'photo')
    success_url = reverse_lazy('blog:index')

    def form_valid(self, form):
        new_blog = form.save(commit=False)
        new_blog.slug = slugify(new_blog.title)
        new_blog.save()
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    """ Редактирует пост блога. """
    model = Blog
    fields = ('title', 'content', 'photo')

    def get_success_url(self):
        return reverse('blog:detail', args=[self.kwargs.get('slug')])


class BlogDeleteView(DeleteView):
    """ Удаляет пост блога.  """
    model = Blog
    success_url = reverse_lazy('blog:index')
