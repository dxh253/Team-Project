from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('posts/', views.PostList.as_view(), name='posts'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
    path('posts/<int:pk>/votes/', views.PostVotesList.as_view(), name='post-votes'),
    path('posts/<int:pk>/votes/<int:id>/', views.PostVotesDetail.as_view(), name='post-vote-detail'),
    path('allposts/', views.AllPostsList.as_view(), name='allposts'),
    path('categories/', views.CategoryList.as_view(), name='categories'),
    path('comments/<int:pk>/', views.CommentDetail.as_view(), name='comment-detail'), # get comment to display
    path('posts/<int:post_pk>/comments/', views.CommentList.as_view(), name='comment-list'), # list comment
    #retrieve comment replies
    # path('posts/<int:post_pk>/comments/<int:comment_pk>/replies/', views.CommentReplyList.as_view(), name='comment-reply-list'),
    path('comments/<int:comment_id>/replies/',views.CommentReplyList.as_view(), name='comment_replies'), # gives all replies in the table
    path('comments/<int:comment_pk>/replies/create/', views.CommentReplyCreateView.as_view(), name='comment-reply-create'), # create reply to top level comment
    path('posts/<int:post_pk>/comments/<int:comment_pk>/replies/<int:reply_pk>/replies/create/', views.CommentReplyCreateView.as_view(), name='comment-reply-reply-create'), # create reply to reply doesn't work and I dont know why
    path('posts/<int:post_pk>/comments/<int:comment_pk>/upvote/', views.CommentUpvoteView.as_view(), name='comment-upvote'),
    path('posts/<int:post_pk>/comments/<int:comment_pk>/downvote/', views.CommentDownvoteView.as_view(), name='comment-downvote'),
    # path('posts/<int:post_pk>/comments/<int:comment_pk>/replies/<int:reply_pk>/upvote/', csrf_exempt(views.CommentReplyUpvoteView.as_view()), name='comment-reply-upvote'),
    path('posts/<int:post_pk>/comments/<int:comment_pk>/replies/<int:reply_pk>/votes/', views.ReplyVoteView.as_view(), name='reply-vote'),
    path('posts/<int:post_pk>/comments/<int:pk>/delete/', views.CommentDelete.as_view(), name='comment-delete'), # delete comment top level
    # path('posts/<int:post_pk>/comments/<int:comment_pk>/replies/<int:reply_pk>/delete/', views.CommentDelete.as_view(), name='comment-reply-delete'),
    path('posts/<int:post_pk>/comments/<int:comment_pk>/replies/<int:pk>/delete/', views.CommentDelete.as_view(), name='comment-reply-delete'), # delete all replies
]

