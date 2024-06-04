from django.shortcuts import render
from .models import Category, Product

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
    return render(request, 'catalog/contacts.html')
