from django.core.mail import send_mail

import my_config


def send_yandex_mail(name_blog):
    """ Отправка письма. """
    send_mail(
        'Просмотры',
        '',
        my_config.yandex_user,
        [my_config.yandex_user],
        fail_silently=False,
        html_message=f'<h2>Поздравляем!!! Блог "{name_blog}" набрал 100 просмотров.</h2>'  # noqa
    )
