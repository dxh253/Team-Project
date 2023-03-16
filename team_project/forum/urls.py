from django.urls import path, include
from .views import ThreadView
from forum import views
from rest_framework_simplejwt.views import ( TokenObtainPairView, TokenRefreshView, )

urlpatterns = [
    path('api-token/', TokenObtainPairView.as_view()),
    path('api-token-refresh/', TokenRefreshView.as_view()),

    path('latest-threads/', views.ThreadList.as_view()),
    path('threads/<slug:category_slug>/<slug:thread_slug>/', views.ThreadDetail.as_view()),
    path('threads/', ThreadView.as_view(), name = 'threadView'),
]