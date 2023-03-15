from django.urls import path, include
from .views import EventsView
from events import views

urlpatterns = [
    path('api/v1/latest-events/', views.EventsList.as_view()),
    path('api/v1/events/<slug:category_slug>/<slug:events_slug>/', views.EventsDetail.as_view()),
    path('api/v1/events/', EventsView.as_view(), name = 'eventsView'),
]
