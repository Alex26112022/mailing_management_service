from django.db import models


class Product(models.Model):
    """ Класс-модель продуктов. """
    title = models.CharField(max_length=100, verbose_name='Наименование',
                             help_text='Введите наименование')
    description = models.TextField(verbose_name='Описание',
                                   help_text='Введите описание', blank=True,
                                   null=True)
    image = models.ImageField(upload_to='products/photo/%Y/%m/%d/',
                              verbose_name='Изображение', blank=True,
                              null=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL,
                                 related_name='product',
                                 verbose_name='Категория', blank=True,
                                 null=True)
    price = models.FloatField(verbose_name='Цена за покупку',
                              help_text='Введите цену за покупку',
                              blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата '
                                                                      'создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата '
                                                                  'последнего изменения')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['-updated_at', 'title']


class Category(models.Model):
    """ Класс-модель категорий. """
    title = models.CharField(max_length=100, verbose_name='Наименование',
                             help_text='Введите наименование')
    description = models.TextField(verbose_name='Описание',
                                   help_text='Введите описание', blank=True,
                                   null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Version(models.Model):
    """ Класс-модель версий. """
    product = models.ForeignKey('Product', on_delete=models.CASCADE,
                                related_name='version', verbose_name='Продукт')
    version = models.FloatField(verbose_name='Версия',
                                help_text='Введите версию')
    title = models.CharField(max_length=100, verbose_name='Название версии',
                             help_text='Введите название версии')
    current_version = models.BooleanField(verbose_name='Текущая версия',
                                          help_text='Это текущая версия?',
                                          default=False)

    def __str__(self):
        return f'{self.title} - {self.version}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'


class Contacts(models.Model):
    """ Класс-модель контактов. """
    title = models.CharField(max_length=100, verbose_name='Название филиала',
                             help_text='Введите название филиала')
    address = models.CharField(max_length=100, verbose_name='Адрес филиала',
                               help_text='Введите адрес филиала')
    phone = models.CharField(max_length=100, verbose_name='Телефон',
                             help_text='Введите телефон', blank=True,
                             null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
