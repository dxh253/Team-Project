from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
import django.contrib.auth.urls
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('reset-password/<str:reset_token>/',
         views.reset_password, name='reset-password'),
    path('forgot-password/', views.forgot_password, name='forgot-password'),
]
