from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import PostSerializer, ScoreSerializer, AllPostsSerializer, PostVotesSerializer, CommentSerializer
from .models import Subreddit, Post, PostVotes, PostComment
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PostVotesList(generics.ListCreateAPIView):
    queryset = PostVotes.objects.all()
    serializer_class = PostVotesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PostVotesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostVotes.objects.all()
    serializer_class = PostVotesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AllPostsList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = AllPostsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CommentList(generics.ListCreateAPIView):
    queryset = PostComment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostComment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# class PostScore(generics.RetrieveAPIView):
#     queryset = Post.objects.all()
#     serializer_class = ScoreSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     lookup_field = 'id'

#     def retrieve(self, request, *args, **kwargs):
#         post = self.get_object()
#         score = post.score()
#         return Response({'score': score})
    
