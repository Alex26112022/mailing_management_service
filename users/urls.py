from django.contrib.auth.views import LoginView, LogoutView, \
    PasswordResetDoneView
from django.urls import path
from django.views.decorators.cache import never_cache

from users.apps import UsersConfig
from users.utils import email_verification
from users.views import UserCreate, notification, MyPasswordReset, ProfileView

app_name = UsersConfig.name

urlpatterns = [
    path("register/", never_cache(UserCreate.as_view()), name='register'),
    path('email-confirm/<str:token>/', email_verification,
         name='email-confirm'),
    path('notification/', notification, name='notification'),
    path('login/', never_cache(LoginView.as_view(template_name='users/login.html')),
         name='login'),
    path('logout/', never_cache(LogoutView.as_view()), name='logout'),
    path('password_reset/', MyPasswordReset.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('profile/', never_cache(ProfileView.as_view()), name='profile'),
]
