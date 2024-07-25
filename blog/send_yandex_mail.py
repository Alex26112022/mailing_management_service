from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER


def send_yandex_mail(name_blog, max_views_count):
    """ Отправка письма. """
    send_mail(
        'Просмотры',
        '',
        EMAIL_HOST_USER,
        [EMAIL_HOST_USER],
        fail_silently=False,
        html_message=f'<h2>Поздравляем!!! Блог "{name_blog}" набрал '
                     f'{max_views_count} просмотров.</h2>'
    )
