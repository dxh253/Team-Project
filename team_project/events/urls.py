from django.urls import path, include
from .views import EventsView
from events import views
from rest_framework_simplejwt.views import ( TokenObtainPairView, TokenRefreshView, )

urlpatterns = [
    path('events/', EventsView.as_view(), name = 'eventsView'),
    path('api-token/', TokenObtainPairView.as_view()),
    path('api-token-refresh/', TokenRefreshView.as_view()),

    path('latest-events/', views.EventsList.as_view()),
    path('events/<slug:category_slug>/<slug:events_slug>/', views.EventsDetail.as_view()),
]
