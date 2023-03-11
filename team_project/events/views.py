from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Events, Category
from .serializers import EventsSerializer, CategorySerializer

class EventsList(APIView):
    def get(self, request, format=None):
        events = Events.objects.all()
        serializer = EventsSerializer(events, many=True)
        return Response(serializer.data)

class EventsDetail(APIView):
    def get_object(self, category_slug, events_slug):
        try:
            return Events.objects.filter(category__slug=category_slug).get(slug=events_slug)
        except Events.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, events_slug, format=None):
        events = self.get_object(category_slug, events_slug)
        serializer = EventsSerializer(events)
        return Response(serializer.data)
        