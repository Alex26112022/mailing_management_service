import json

from django.core.management import BaseCommand

from blog.models import Blog
from catalog.models import Product, Category, Contacts
from my_config import path_fixture_json, path_blog_fixture_json


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
        with open(path_fixture_json, encoding='utf-8') as f_prod:
            data_prod = json.load(f_prod)
        list_products = []
        for el in data_prod:
            if el['model'] == "catalog.product":
                list_products.append(el)
        return list_products

    @staticmethod
    def json_read_contacts():
        """ Получает данные из фикстур с контактами. """
        with open(path_fixture_json, encoding='utf-8') as f_con:
            data_prod = json.load(f_con)
        list_contacts = []
        for el in data_prod:
            if el['model'] == "catalog.contacts":
                list_contacts.append(el)
        return list_contacts

    @staticmethod
    def json_read_blog():
        """ Получает данные из фикстур с блогами. """
        with open(path_blog_fixture_json, encoding='utf-8') as f_blog:
            data_blog = json.load(f_blog)
        list_blog = []
        for el in data_blog:
            list_blog.append(el)
        return list_blog

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()
        Contacts.objects.all().delete()
        Blog.objects.all().delete()

        product_for_create = []
        category_for_create = []
        contact_for_create = []
        blog_for_create = []

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

        for blog in self.json_read_blog():
            blog_for_create.append(Blog(pk=blog.get('pk'),
                                        title=blog.get(
                                            'fields').get('title'),
                                        slug=blog.get('fields').get('slug'),
                                        content=blog.get(
                                            'fields').get('content'),
                                        photo=blog.get(
                                            'fields').get('photo'),
                                        created_at=blog.get(
                                            'fields').get('created_at'),
                                        is_published=blog.get('fields').get(
                                            'is_published'),
                                        count=blog.get('fields').get(
                                            'count'), ))

        Blog.objects.bulk_create(blog_for_create)
