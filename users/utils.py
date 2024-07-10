from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
import string
import random


def email_verification(request, token):
    """ Проверка почты. """
    user = get_object_or_404(get_user_model(), token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


def generate_password(length):
    """ Генератор пароля. """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
