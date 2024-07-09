import secrets

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm


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
        print(host)
        url = f'http://{host}/users/email-confirm/{token}/'
        send_mail(subject='Подтверждение почты',
                  message=f'Пожалуйста, подтвердите вашу почту. '
                          f'Перейдите по ссылке: {url}',
                  from_email=EMAIL_HOST_USER,
                  recipient_list=[user.email])
        return super().form_valid(form)


