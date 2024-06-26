# Generated by Django 5.0.6 on 2024-06-19 17:59

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('title',
                 models.CharField(max_length=100, verbose_name='Заголовок')),
                ('slug',
                 models.CharField(blank=True, max_length=100, null=True,
                                  verbose_name='Слаг')),
                ('content', models.TextField(blank=True, null=True,
                                             verbose_name='Содержание')),
                ('photo', models.ImageField(blank=True, null=True,
                                            upload_to='blog/photo/%Y/%m/%d/',
                                            verbose_name='Изображение')),
                ('created_at', models.DateTimeField(auto_now_add=True,
                                                    verbose_name='Дата '
                                                                 'создания')),
                ('is_published', models.BooleanField(default=True,
                                                     verbose_name='Опубликовано')),  # noqa: E501
                ('count', models.PositiveIntegerField(default=0,
                                                      verbose_name='Количество просмотров')),  # noqa: E501
            ],
        ),
    ]
