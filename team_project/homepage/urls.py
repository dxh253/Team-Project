from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('register/', views.register_user, name='register'),
    # path('forgot-password/', views.forgot_password, name='forgot_password'),
    # path('reset-password/<str:token>/', csrf_exempt(views.reset_password), name='reset_password'),
    path('reset-password/<str:token>/',
         views.reset_password, name='reset_password'),

]
