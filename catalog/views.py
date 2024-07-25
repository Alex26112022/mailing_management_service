from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, \
    DeleteView, TemplateView
from django.core.paginator import Paginator
from .models import Category, Product, Contacts, Version
from .forms import ProductForm, VersionForm, ProductModeratorForm

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
        try:
            context['version'] = Version.objects.filter(
                current_version=True).get(
                product=self.object)
        except Version.DoesNotExist:
            context['version'] = None
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    """ Создает новый продукт. """
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')

    def form_valid(self, form):
        product = form.save(commit=False)
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """ Редактирует продукт. """
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        VersionFormSet = inlineformset_factory(Product, Version, VersionForm,
                                               extra=1)
        if self.request.method == 'POST':
            context['formset'] = VersionFormSet(self.request.POST,
                                                instance=self.object)
        else:
            context['formset'] = VersionFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(
                self.get_context_data(form=form, formset=formset))

    def get_form_class(self):
        user = self.request.user
        if user.groups.filter(name='moderator').exists():
            return ProductModeratorForm
        else:
            return ProductForm


class ProductDeleteView(LoginRequiredMixin, DeleteView):
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
