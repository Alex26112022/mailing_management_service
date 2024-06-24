from django.db import models
from pytils.translit import slugify


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.CharField(max_length=100, null=True, blank=True,
                            verbose_name='Слаг', auto_created=slugify(title),
                            db_index=True)
    content = models.TextField(verbose_name='Содержание', blank=True,
                               null=True)
    photo = models.ImageField(upload_to='blog/photo/%Y/%m/%d/',
                              verbose_name='Изображение', blank=True,
                              null=True)
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Дата создания')
    is_published = models.BooleanField(default=True,
                                       verbose_name='Опубликовано')
    views_count = models.PositiveIntegerField(default=0,
                                              verbose_name='Количество '
                                                           'просмотров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ['-created_at']
