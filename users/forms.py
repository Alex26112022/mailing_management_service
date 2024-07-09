from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from catalog.forms import StyleFormMixin


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'password1', 'password2']
