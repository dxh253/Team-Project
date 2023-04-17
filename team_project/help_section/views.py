from django.shortcuts import render
from .models import Problems
from django.http import HttpResponse

from rest_framework import generics
from .serializers import ProblemSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class ProblemsView(generics.RetrieveAPIView):
    queryset = Problems.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ProblemSerializer(queryset, many=True)
        return Response(serializer.data)
