from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Contacts

from catalog.write_csv import write_csv


def index(request):
    data_products = Product.objects.all()
    print(data_products[:5])
    return render(request, 'catalog/index.html',
                  {'data_products': data_products[:5]})


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
