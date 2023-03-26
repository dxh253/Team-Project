

from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostList.as_view(), name='posts'),
    path('posts/<slug:title>/', views.PostDetail.as_view(), name='post-detail'),
    path('posts/<int:pk>/votes/', views.PostVotesList.as_view(), name='post-votes'),
    path('posts/<int:pk>/votes/<int:id>/', views.PostVotesDetail.as_view(), name='post-vote-detail'),
    path('allposts/', views.AllPostsList.as_view(), name='allposts'),
    path('comments/', views.CommentList.as_view(), name='comments'),
    path('comments/<int:pk>/', views.CommentDetail.as_view(), name='comment-detail'),
    # path('posts/<int:id>/score/', views.PostScore.as_view(), name='post-score'),

]