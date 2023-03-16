from django.urls import path, include
from .views import ForumDetail, ThreadView
from forum import views
from rest_framework_simplejwt.views import ( TokenObtainPairView, TokenRefreshView, )

urlpatterns = [
    path('api-token/', TokenObtainPairView.as_view()),
    path('api-token-refresh/', TokenRefreshView.as_view()),

    path('forums/', views.ForumDetail.as_view()),
    path('forums/<slug:category_slug>/<slug:forum_slug>/', views.ForumDetail.as_view()),
    path('forums/<slug:forum_slug>/threads/', views.ThreadList.as_view()),
    path('forums/<slug:forum_slug>/threads/<slug:thread_slug>/', views.ThreadDetail.as_view()),
    path('threads/<int:pk>/', ThreadView.as_view()),
]