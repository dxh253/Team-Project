from django.urls import path
from .views import obtain_token, refresh_token

urlpatterns = [
    path('api/token/', obtain_token, name='token_obtain_pair'),
    path('api/token/refresh/', refresh_token, name='token_refresh'),
]
