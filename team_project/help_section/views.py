from django.shortcuts import render
from .models import Problems
from django.http import HttpResponse

from rest_framework import generics
from .serializers import ProblemSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class ProblemsView(APIView):
    permission_classes = (IsAuthenticated,)
    ALLOWED_METHODS = ['GET', 'POST']
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        queryset = Problems.objects.all()
        serializer = ProblemSerializer(queryset, many=True)
        return Response(serializer.data)

    def post():
        return