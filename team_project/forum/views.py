from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Forum, Thread, Post
from rest_framework import generics
from .serializers import ThreadSerializer, ForumSerializer, PostSerializer
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.utils.text import slugify
from django.utils.datastructures import MultiValueDict
from django.shortcuts import get_object_or_404

class ForumDetail(generics.RetrieveAPIView):
    def get(self, request, category_slug, forum_slug, format=None):
        forum = get_object_or_404(Forum, category__slug=category_slug, slug=forum_slug)
        serializer = ForumSerializer(forum)
        return Response(serializer.data)
    
class ForumView(generics.RetrieveAPIView):
    serializer_class = ThreadSerializer

    def get_queryset(self):
        forum_slug = self.kwargs['forum_slug']
        forum = Forum.objects.get(slug=forum_slug)
        return Thread.objects.filter(forum=forum)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['forum'] = ForumSerializer(Forum.objects.get(slug=self.kwargs['forum_slug'])).data
        return context
    
class ThreadList(generics.ListCreateAPIView):
    def get(self, request, forum_slug, format=None):
        threads = Thread.objects.filter(forum__slug=forum_slug)
        serializer = ThreadSerializer(threads, many=True)
        return Response(serializer.data)
    
    def post(self, request, forum_slug, format=None):
        data = request.data.copy()
        data['forum'] = Forum.objects.get(slug=forum_slug).id
        serializer = ThreadSerializer(data=data)
        if serializer.is_valid():
            instance = serializer.save()
            instance.slug = slugify(f"{instance.id}-{instance.name}")
            instance.save()

            if 'image' in request.FILES:
                image = request.FILES['image']
                image_name = f"{instance.slug}-{image.name}"
                with open(image_name, 'wb+') as f:
                    for chunk in image.chunks():
                        f.write(chunk)
                instance.image = image_name
                instance.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ThreadDetail(generics.RetrieveUpdateDestroyAPIView):
    def get(self, request, forum_slug, thread_slug, format=None):
        thread = get_object_or_404(Thread, forum__slug=forum_slug, slug=thread_slug)
        serializer = ThreadSerializer(thread)
        return Response(serializer.data)

class ThreadView(generics.RetrieveAPIView):
    queryset = Thread.objects.all()

    def get(self, request, pk, format=None):
        thread = self.get_object(pk)
        serializer = ThreadSerializer(thread)
        return Response(serializer.data)
    
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer = PostSerializer(queryset, many=True)

    def get(self, request, thread_slug, format=None):
        posts = Post.objects.filter(thread__slug=thread_slug)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    def post(self, request, thread_slug, format=None):
        data = request.data.copy()
        data['thread'] = Thread.objects.get(slug=thread_slug).id
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    def get_object(self, thread_slug, post_slug):
        try:
            return Post.objects.filter(thread__slug=thread_slug).get(slug=post_slug)
        except Post.DoesNotExist:
            raise Http404
    
    def get(self, request, thread_slug, post_slug, format=None):
        post = self.get_object(thread_slug, post_slug)
        serializer = PostSerializer(post)
        return Response(serializer.data)
