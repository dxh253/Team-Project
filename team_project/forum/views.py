from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import PostSerializer, AllPostsSerializer, PostVotesSerializer, CommentSerializer
from .models import Subreddit, Post, PostVotes, PostComment
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PostVotesList(generics.ListCreateAPIView):
    queryset = PostVotes.objects.all()
    serializer_class = PostVotesSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        user_id = self.request.query_params.get('user_id')
        if user_id:
            queryset = PostVotes.objects.filter(post_id=pk, user_id=user_id)
        else:
            queryset = PostVotes.objects.filter(post_id=pk)
        return queryset
    

class PostVotesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostVotes.objects.all()
    serializer_class = PostVotesSerializer
    lookup_url_kwarg = 'id'
    lookup_field = 'id'

    def get_queryset(self):
        post_id = self.kwargs['pk']
        id = self.kwargs['id']
        return PostVotes.objects.filter(post_id=post_id, id=id)
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

class AllPostsList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = AllPostsSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CommentList(generics.ListCreateAPIView):
    queryset = PostComment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostComment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    
