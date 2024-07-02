from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, \
    DeleteView, TemplateView
from django.core.paginator import Paginator
from .models import Category, Product, Contacts, Version
from .forms import ProductForm

from catalog.write_csv import write_csv


class ProductListView(ListView):
    """ Выводит список всех продуктов. """
    model = Product
    paginate_by = 4


class ProductDetailView(DetailView):
    """ Выводит детальную страницу продукта. """
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # versions = Version.objects.filter(current_version=True)
        # context['version'] = versions.get(product=self.object)
        # if versions.get(product=self.object).current_version:
        #     context['version'] = versions.get(product=self.object)
        try:
            context['version'] = Version.objects.filter(current_version=True).get(
                product=self.object)
        except Version.DoesNotExist:
            context['version'] = None
        return context


class ProductCreateView(CreateView):
    """ Создает новый продукт. """
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')


class ProductUpdateView(UpdateView):
    """ Редактирует продукт. """
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')


class ProductDeleteView(DeleteView):
    """ Удаляет продукт. """
    model = Product
    success_url = reverse_lazy('catalog:index')


class ContactlistView(ListView):
    """ Выводит список контактов. """
    model = Contacts

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        write_csv(name, phone, message)

        print(f'Имя пользователя: {name}\n'
              f'Телефон: {phone}\n'
              f'Сообщение: {message}\n')

        return HttpResponseRedirect(reverse('catalog:contacts'))
