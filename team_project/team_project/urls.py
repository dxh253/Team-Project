from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from homepage.views import register_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/events/', include('events.urls')),
    path('api/v1/register/', register_user),
    path('', include('events.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
