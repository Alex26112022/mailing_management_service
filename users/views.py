import secrets

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm
from users.utils import generate_password


def notification(request):
    return render(request, 'users/notification.html')


class UserCreate(CreateView):
    """ Создает нового пользователя. """
    model = get_user_model()
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:notification')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        send_mail(subject='Подтверждение почты',
                  message=f'Пожалуйста, подтвердите вашу почту. '
                          f'Перейдите по ссылке: {url}',
                  from_email=EMAIL_HOST_USER,
                  recipient_list=[user.email])
        return super().form_valid(form)


class MyPasswordReset(PasswordResetView):
    """ Сброс пароля пользователей. """
    template_name = 'users/password_reset_form.html'

    def form_valid(self, form):
        email = form.cleaned_data['email']
        user = get_object_or_404(get_user_model(), email=email)
        new_password = generate_password(8)
        hash_new_password = make_password(new_password)
        user.password = hash_new_password
        user.save()
        send_mail(subject='Сброс пароля',
                  message='',
                  from_email=EMAIL_HOST_USER,
                  recipient_list=[user.email],
                  html_message=f'<h3>Старый пароль успешно сброшен. '
                               f'Ваш новый пароль: <h2><b>{new_password}</b></h2></h3>')

        return HttpResponseRedirect(reverse('users:password_reset_done'))
