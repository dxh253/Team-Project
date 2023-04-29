from django.shortcuts import render
from .models import Problems, Comment
from django.http import HttpResponse
from django.http import Http404

from rest_framework import generics
from .serializers import ProblemSerializer, CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# Create your views here.


class ProblemsView(APIView):
    permission_classes = (IsAuthenticated,)
    ALLOWED_METHODS = ['GET', 'POST']
    http_method_names = ['get', 'post']

    def get(self, request, format=None):
        queryset = Problems.objects.all()
        serializer = ProblemSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data.copy()
        serializer = ProblemSerializer(data=data)
        if serializer.is_valid():
            instance = serializer.save()
            instance.save()
            serializer = ProblemSerializer(instance)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProblemsDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, problem_id):
        print(self.request.user)
        # print(APIView.request.user)
        try:
            return Problems.objects.get(id=problem_id)
        except Problems.DoesNotExist:
            raise Http404

    def get(self, request, problem_id, format=None):
        problems = self.get_object(problem_id)
        serializer = ProblemSerializer(problems)
        return Response(serializer.data)

    def delete(self, request, problem_id, format=None):
        problems = self.get_object(problem_id)

        # Check if the authenticated user is the owner of the event
        if problems.owner != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        problems.delete_problem()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer

    def get(self, request, problem_id):
        # This view should return a list of all the comments for the post as determined by the post_pk portion of the URL.
        queryset = Comment.objects.filter(problem=problem_id)
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, problem_id):
        data = request.data.copy()
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            instance = serializer.save()
            instance.save()
            serializer = CommentSerializer(instance)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, problem_id, comment_id):
        comments = Comment.objects.get(problem=problem_id, id=comment_id)

        comments.delete_comment()
        return Response(status=status.HTTP_204_NO_CONTENT)