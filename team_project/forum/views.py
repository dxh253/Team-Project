# from rest_framework import generics, permissions, status
# from rest_framework.response import Response
# from .serializers import PostSerializer, AllPostsSerializer, PostVotesSerializer, CommentSerializer, CategorySerializer
# from .models import Category, Post, PostVotes, PostComment
# from django.http import JsonResponse
# from django.shortcuts import get_object_or_404


# class PostList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)


# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# class PostVotesList(generics.ListCreateAPIView):
#     queryset = PostVotes.objects.all()
#     serializer_class = PostVotesSerializer
#     # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#         user_id = self.request.query_params.get('user_id')
#         if user_id:
#             queryset = PostVotes.objects.filter(post_id=pk, user_id=user_id)
#         else:
#             queryset = PostVotes.objects.filter(post_id=pk)
#         return queryset

#     def post(self, request, pk):
#         user_id = request.data.get('user_id')
#         vote_value = request.data.get('vote')
#         if user_id is None or vote_value is None:
#             return Response({'error': 'Invalid request.'}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             vote = PostVotes.objects.get(user_id=user_id, post_id=pk)
#             vote.vote = vote_value
#             vote.save()
#             serializer = PostVotesSerializer(vote)
#         except PostVotes.DoesNotExist:
#             data = {'user_id': user_id, 'vote': vote_value, 'post_id': pk}
#             serializer = PostVotesSerializer(data=data)
#             if serializer.is_valid():
#                 serializer.save()
#             else:
#                 return Response({'error': 'Invalid request.'}, status=status.HTTP_400_BAD_REQUEST)

#         return Response(serializer.data)


# class PostVotesDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = PostVotes.objects.all()
#     serializer_class = PostVotesSerializer
#     lookup_url_kwarg = 'id'
#     lookup_field = 'id'

#     def get_queryset(self):
#         post_id = self.kwargs['pk']
#         id = self.kwargs['id']
#         return PostVotes.objects.filter(post_id=post_id, id=id)
#     # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(
#             instance, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
#         return Response(serializer.data)


# class AllPostsList(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = AllPostsSerializer
#     # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# class CommentList(generics.ListCreateAPIView):
#     queryset = PostComment.objects.all()
#     serializer_class = CommentSerializer
#     # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def perform_create(self, serializer):
#         serializer.save(user_id=self.request.user)


# class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = PostComment.objects.all()
#     serializer_class = CommentSerializer
#     # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# class CategoryList(generics.ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def post(self, request):
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import PostSerializer, AllPostsSerializer, PostVotesSerializer, CommentSerializer, CategorySerializer
from .models import Category, Post, PostVotes, PostComment
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

# Add this import
from rest_framework_simplejwt.authentication import JWTAuthentication

# Define a custom permission class


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class PostVotesList(generics.ListCreateAPIView):
    queryset = PostVotes.objects.all()
    serializer_class = PostVotesSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        user_id = self.request.query_params.get('user_id')
        if user_id:
            queryset = PostVotes.objects.filter(post_id=pk, user_id=user_id)
        else:
            queryset = PostVotes.objects.filter(post_id=pk)
        return queryset

    def post(self, request, pk):
        user_id = request.data.get('user_id')
        vote_value = request.data.get('vote')
        if user_id is None or vote_value is None:
            return Response({'error': 'Invalid request.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            vote = PostVotes.objects.get(user_id=user_id, post_id=pk)
            vote.vote = vote_value
            vote.save()
            serializer = PostVotesSerializer(vote)
        except PostVotes.DoesNotExist:
            data = {'user_id': user_id, 'vote': vote_value, 'post_id': pk}
            serializer = PostVotesSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response({'error': 'Invalid request.'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data)


class PostVotesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostVotes.objects.all()
    serializer_class = PostVotesSerializer
    lookup_url_kwarg = 'id'
    lookup_field = 'id'
    authentication_classes = [JWTAuthentication]
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs['pk']
        id = self.kwargs['id']
        return PostVotes.objects.filter(post_id=post_id, id=id)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class AllPostsList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = AllPostsSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CommentList(generics.ListCreateAPIView):
    queryset = PostComment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostComment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
