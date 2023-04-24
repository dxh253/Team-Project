from django.urls import path
from .views import ProblemsDetail, ProblemsView
from help_section import views


from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('api-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api-token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/help/<int:problem_id>/', views.ProblemsDetail.as_view()),
    path('api/v1/help/', views.ProblemsView.as_view(), name="ProblemView"),
]
