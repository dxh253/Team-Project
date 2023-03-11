from django.urls import path, include

from events import views

urlpatterns = [
    path('latest-events/', views.EventsList.as_view()),
    path('events/<slug:category_slug>/<slug:events_slug>/', views.EventsDetail.as_view()),
]
