# from .views import register_user
# from django.contrib.auth.views import LoginView, LogoutView
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register_user, name='register'),
    # path('/api-token/', TokenObtainPairView.as_view()),
    # path('/api-token-refresh/', TokenRefreshView.as_view())
]
