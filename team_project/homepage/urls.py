from django.urls import path
from . import views 
from . views import homepage

urlpatterns = [
    path('homepage/', views.homepage, name='home'),
    # path('homepage/', homepage, name='home'),
]

