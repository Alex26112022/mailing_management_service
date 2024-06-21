# Generated by Django 5.0.6 on 2024-06-04 08:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('title', models.CharField(help_text='Введите наименование',
                                           max_length=100,
                                           verbose_name='Наименование')),
                ('description',
                 models.TextField(blank=True, help_text='Введите описание',
                                  null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('title', models.CharField(help_text='Введите наименование',
                                           max_length=100,
                                           verbose_name='Наименование')),
                ('description',
                 models.TextField(blank=True, help_text='Введите описание',
                                  null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True,
                                            upload_to='products/photo/%Y/%m/%d/',  # noqa
                                            verbose_name='Изображение')),
                ('price', models.FloatField(blank=True,
                                            help_text='Введите цену за '
                                                      'покупку',
                                            null=True,
                                            verbose_name='Цена за покупку')),
                ('created_at', models.DateTimeField(auto_now_add=True,
                                                    verbose_name='Дата '
                                                                 'создания')),
                ('updated_at', models.DateTimeField(auto_now=True,
                                                    verbose_name='Дата '
                                                                 'последнего изменения')),  # noqa
                ('category', models.ForeignKey(blank=True, null=True,
                                               on_delete=django.db.models.deletion.SET_NULL,  # noqa
                                               related_name='product',
                                               to='catalog.category',
                                               verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ['-updated_at', 'title'],
            },
        ),
    ]
