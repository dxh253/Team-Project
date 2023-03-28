from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from homepage.views import register_user
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('api/v1/register/', register_user),
    path('api-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api-token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('', include('events.urls')),
    path('', include('authentication.urls')),
    path('events/', include('events.urls')),
    path('api/admin/', admin.site.urls, name='admin'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


