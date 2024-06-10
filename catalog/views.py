from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from django.core.paginator import Paginator
from .models import Category, Product, Contacts
from .forms import ProductForm

from catalog.write_csv import write_csv


def index(request):
    data_products = Product.objects.all()
    paginator = Paginator(data_products, 4)
    print(data_products)
    if 'page' in request.GET:
        page_num = request.GET.get('page')
    else:
        page_num = 1
    page_obj = paginator.get_page(page_num)
    return render(request, 'catalog/index.html',
                  {'page_obj': page_obj})


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        write_csv(name, phone, message)

        print(f'Имя пользователя: {name}\n'
              f'Телефон: {phone}\n'
              f'Сообщение: {message}\n')

    data_contacts = Contacts.objects.all()

    return render(request, 'catalog/contacts.html',
                  {'data_contacts': data_contacts})


def get_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'catalog/product.html', context)


class ProductCreateView(CreateView):
    template_name = 'catalog/add_product.html'
    form_class = ProductForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context
