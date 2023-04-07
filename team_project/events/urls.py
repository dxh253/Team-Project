from django.urls import path, include
from .views import EventsView, SaveEvent, SavedEventsView
from events import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('api-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api-token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/latest-events/', views.EventsList.as_view()),
    path('api/v1/events/<slug:category_slug>/<slug:events_slug>/', views.EventsDetail.as_view()),
    path('api/v1/events/', EventsView.as_view(), name='eventsView'),
    path('api/v1/save-event/', SaveEvent.as_view(), name='saveEvent'),
    path('api/v1/saved-events/', SavedEventsView.as_view(), name='savedEventsView'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)