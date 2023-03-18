from django.urls import path, include
from .views import ForumDetail, ThreadView, ForumView, ThreadList, ThreadDetail
from forum import views
from rest_framework_simplejwt.views import ( TokenObtainPairView, TokenRefreshView, )

urlpatterns = [
    path('api-token/', TokenObtainPairView.as_view()),
    path('api-token-refresh/', TokenRefreshView.as_view()),

    path('api/v1/forums/', ForumView.as_view(), name = 'forumView'),   

]