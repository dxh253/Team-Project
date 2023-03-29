from django.urls import path, include
from .views import EventsView
from events import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('api-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api-token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/events/', EventsView.as_view(), name = 'eventsView'),
    # path('latest-events/', views.EventsList.as_view(), name = 'latestEvents'),
    # path('events/<slug:category_slug>/<slug:events_slug>/', views.EventsDetail.as_view()),
    path('api/v1/latest-events/', views.EventsList.as_view()),
    path('api/v1/events/<slug:category_slug>/<slug:events_slug>/',
        views.EventsDetail.as_view()),
    path('api/v1/events/', EventsView.as_view(), name='eventsView'),
    path('api/v1/events/<slug:category_slug>', views.CategoryDetail.as_view()),
]


# urlpatterns = [
#     path('api-token/', TokenObtainPairView.as_view()),
#     path('api-token-refresh/', TokenRefreshView.as_view()),

#     path('latest-events/', views.EventsList.as_view()),
#     path('events/<slug:category_slug>/<slug:events_slug>/', views.EventsDetail.as_view()),
#     path('events/', EventsView.as_view(), name='eventsView'),
# ]
