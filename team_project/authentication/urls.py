from django.urls import path
from .views import obtain_token, refresh_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    # path('api/token/', obtain_token, name='token_obtain_pair'),
    # path('api/token/refresh/', refresh_token, name='token_refresh'),
    path('api-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api-token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
