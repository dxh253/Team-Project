from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/problems', views.ProblemsView.as_view()),
]
