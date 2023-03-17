from django.urls import path, include
from .views import ForumDetail, ThreadView, ForumView, ThreadList, ThreadDetail
from forum import views
from rest_framework_simplejwt.views import ( TokenObtainPairView, TokenRefreshView, )

urlpatterns = [
    path('api-token/', TokenObtainPairView.as_view()),
    path('api-token-refresh/', TokenRefreshView.as_view()),

    path('forums/', views.ForumView.as_view()),
    path('forums/<int:pk>/', ForumDetail.as_view(), name='forum-detail'),
    path('forums/<int:pk>/threads/', ThreadList.as_view(), name='thread-list'),
    path('forums/<int:forum_pk>/threads/<int:pk>/', ThreadDetail.as_view(), name='thread-detail'),
    path('forums/<int:pk>/threads/create/', ThreadView.as_view(), name='thread-create'),
]