from django.shortcuts import render
from .models import Problems
from django.http import HttpResponse

from rest_framework import generics
from .serializers import ProblemSerializer
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