# from django.shortcuts import render
# from django.views.generic import ListView, DetailView, TemplateView, CreateView
# from .models import Subreddit, Post

# from rest_framework.views import APIView
# from rest_framework.response import Response

# from .serializers import PostSerializer, PostVotesSerializer, AllPostsSerializer
# from rest_framework import generics

# class PostView(generics.RetrieveAPIView):
#     model = Post
#     slug_field = 'slug'
#     slug_url_kwarg = 'slug'
#     template_name = 'posts/post_view.html'

#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         # Add in a QuerySet of all the data
#         context['subreddits'] = Subreddit.objects.all()
#         return context

# class SubredditView(DetailView):
#     model = Subreddit
#     template_name = 'posts/subreddit_view.html'

#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         # Add in a QuerySet of all the data
#         obj = self.get_object().id
#         context['posts'] = Post.objects.filter(subreddit=obj)
#         context['subreddits'] = Subreddit.objects.all()
#         return context

# class AllSubredditsView(TemplateView):
#     model = Subreddit
#     template_name = 'posts/subreddit_view.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['posts'] = Post.objects.all()
#         context['subreddits'] = Subreddit.objects.all()
#         context['page'] = "all"
#         return context

# class FrontPageView(TemplateView):
#     model = Subreddit
#     template_name = 'posts/subreddit_view.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['posts'] = Post.objects.all()
#         context['subreddits'] = Subreddit.objects.all()
#         context['page'] = "frontpage"
#         return context

from rest_framework import generics
from .models import Subreddit, Post, PostVotes, PostComment
from .serializers import PostSerializer, PostVotesSerializer, AllPostsSerializer, CommentSerializer

class PostAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'title'

class AllPostsAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = AllPostsSerializer

class CommentAPIView(generics.ListCreateAPIView):
    queryset = PostComment.objects.all()
    serializer_class = CommentSerializer

class CommentDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostComment.objects.all()
    serializer_class = CommentSerializer
