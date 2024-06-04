import json

from django.core.management import BaseCommand

from catalog.models import Product, Category, Contacts
from my_config import path_fixture_json


class Command(BaseCommand):
    """ Класс заполнения БД. """

    @staticmethod
    def json_read_categories():
        """ Получает данные из фикстур с категориями. """
        with open(path_fixture_json, encoding='utf-8') as f_cat:
            data_cat = json.load(f_cat)
        list_categories = []
        for el in data_cat:
            if el['model'] == "catalog.category":
                list_categories.append(el)
        return list_categories

    @staticmethod
    def json_read_products():
        """ Получает данные из фикстур с продуктами. """
        with open(path_fixture_json, encoding='utf-8') as f_cat:
            data_cat = json.load(f_cat)
        list_products = []
        for el in data_cat:
            if el['model'] == "catalog.product":
                list_products.append(el)
        return list_products

    @staticmethod
    def json_read_contacts():
        """ Получает данные из фикстур с контактами. """
        with open(path_fixture_json, encoding='utf-8') as f_cat:
            data_cat = json.load(f_cat)
        list_contacts = []
        for el in data_cat:
            if el['model'] == "catalog.contacts":
                list_contacts.append(el)
        return list_contacts

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()
        Contacts.objects.all().delete()

        product_for_create = []
        category_for_create = []
        contact_for_create = []

        for category in self.json_read_categories():
            category_for_create.append(Category(pk=category.get('pk'),
                                                title=category.get(
                                                    'fields').get('title'),
                                                description=category.get(
                                                    'fields').get(
                                                    'description')))

        Category.objects.bulk_create(category_for_create)

        for product in self.json_read_products():
            product_for_create.append(Product(pk=product.get('pk'),
                                              title=product.get(
                                                  'fields').get('title'),
                                              description=product.get(
                                                  'fields').get(
                                                  'description'),
                                              image=product.get(
                                                  'fields').get('image'),
                                              category=Category.objects.get(
                                                  pk=product.get(
                                                      'fields').get(
                                                      'category')),
                                              price=product.get(
                                                  'fields').get('price'),
                                              created_at=product.get(
                                                  'fields').get(
                                                  'created_at'),
                                              updated_at=product.get(
                                                  'fields').get('updated_at')))

        Product.objects.bulk_create(product_for_create)

        for contact in self.json_read_contacts():
            contact_for_create.append(Contacts(pk=contact.get('pk'),
                                               title=contact.get(
                                                   'fields').get('title'),
                                               address=contact.get(
                                                   'fields').get('address'),
                                               phone=contact.get(
                                                   'fields').get('phone')))

        Contacts.objects.bulk_create(contact_for_create)
