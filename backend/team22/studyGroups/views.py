from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import StudyGroup
from .serializers import StudyGroupSerializer


class StudyGroupView(generics.RetrieveAPIView):
    queryset = StudyGroup.objects.all()

    def get(self, request):
        queryset = self.get_queryset()
        serializer = StudyGroupSerializer(queryset, many=True)
        return Response(serializer.data)
