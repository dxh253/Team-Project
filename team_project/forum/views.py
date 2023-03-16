from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Thread, Category
from rest_framework import generics
from .serializers import ThreadSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.utils.text import slugify
from django.utils.datastructures import MultiValueDict

class ThreadList(APIView):
    def get(self, request, format=None):
        threads = Thread.objects.all()
        serializer = ThreadSerializer(threads, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        data = request.data.copy()  # Create a mutable copy of the QueryDict
        data['category'] = 1  # Modify the category field
        serializer = ThreadSerializer(data=data)
        if serializer.is_valid():
            instance = serializer.save()
            instance.slug = slugify(f"{instance.id}-{instance.title}")
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
    
class ThreadDetail(APIView):
    def get_object(self, category_slug, thread_slug):
        try:
            return Thread.objects.filter(category__slug=category_slug).get(slug=thread_slug)
        except Thread.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, thread_slug, format=None):
        thread = self.get_object(category_slug, thread_slug)
        serializer = ThreadSerializer(thread)
        return Response(serializer.data)
    
class ThreadView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Thread.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        thread = generics.get_object_or_404(queryset, pk=kwargs['pk'])
        serializer = ThreadSerializer(thread)
        return Response(serializer.data)



