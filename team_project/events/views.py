from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Events, Category
from rest_framework import generics
from .serializers import EventsSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.utils.text import slugify
from django.utils.datastructures import MultiValueDict


class EventsList(APIView):
    def get(self, request, format=None):
        events = Events.objects.all()
        serializer = EventsSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data.copy()  # Create a mutable copy of the QueryDict
        data['category'] = 1  # Modify the category field
        serializer = EventsSerializer(data=data)
        if serializer.is_valid():
            instance = serializer.save()
            instance.slug = slugify(f"{instance.id}-{instance.name}")
            instance.save()

            # Save the image file if it exists in the request.FILES dictionary
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


class EventsView(generics.RetrieveAPIView):
    queryset = Events.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = EventsSerializer(queryset, many=True)
        return Response(serializer.data)


class CreateEventView(generics.CreateAPIView):
    serializer_class = EventsSerializer
    queryset = Events.objects.all()
