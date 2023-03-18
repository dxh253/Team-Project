# from django.http import Http404

# from rest_framework.views import APIView
# from rest_framework.response import Response

# from .models import Events, Category
# from rest_framework import generics
# from .serializers import EventsSerializer, CategorySerializer
# from rest_framework.permissions import IsAuthenticated
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework import status
# from django.utils.text import slugify
# from django.utils.datastructures import MultiValueDict
# class EventsList(APIView):
#     def get(self, request, format=None):
#         events = Events.objects.all()
#         serializer = EventsSerializer(events, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         data = request.data.copy()  # Create a mutable copy of the QueryDict
#         data['category'] = 1  # Modify the category field
#         serializer = EventsSerializer(data=data)
#         if serializer.is_valid():
#             instance = serializer.save()
#             instance.slug = slugify(f"{instance.id}-{instance.name}")
#             instance.save()

#             # Save the image file if it exists in the request.FILES dictionary
#             if 'image' in request.FILES:
#                 image = request.FILES['image']
#                 image_name = f"{instance.slug}-{image.name}"
#                 with open(image_name, 'wb+') as f:
#                     for chunk in image.chunks():
#                         f.write(chunk)
#                 instance.image = image_name
#                 instance.save()

#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class EventsDetail(APIView):
#     def get_object(self, category_slug, events_slug):
#         try:
#             return Events.objects.filter(category__slug=category_slug).get(slug=events_slug)
#         except Events.DoesNotExist:
#             raise Http404
    
#     def get(self, request, category_slug, events_slug, format=None):
#         events = self.get_object(category_slug, events_slug)
#         serializer = EventsSerializer(events)
#         return Response(serializer.data)
        

# class EventsView(generics.RetrieveAPIView):
#     queryset = Events.objects.all()

#     def get(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         serializer = EventsSerializer(queryset, many=True)
#         return Response(serializer.data)
    
    
# class CreateEventView(generics.CreateAPIView):
#     serializer_class = EventsSerializer
#     queryset = Events.objects.all()



# from django.http import Http404

# from rest_framework.views import APIView
# from rest_framework.response import Response

# from .models import Events, Category
# from rest_framework import generics
# from .serializers import EventsSerializer, CategorySerializer
# from rest_framework.permissions import IsAuthenticated
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework import status
# from django.utils.text import slugify
# from django.utils.datastructures import MultiValueDict
# from io import BytesIO
# from PIL import Image
# from azure.storage.blob import BlobServiceClient

# AZURE_ACCOUNT_NAME = 'teamproject'
# AZURE_ACCOUNT_KEY = 'TvugZzDaTGkdgnZKQwzOsSjgdLcWongNPR433WCqOwLI+jN4GRV/R1gRUapBbbkD4VGm47QaVON0+AStdea6TA=='
# AZURE_CONTAINER_NAME = 'events'

# AZURE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=%s;AccountKey=%s;EndpointSuffix=core.windows.net" % (AZURE_ACCOUNT_NAME, AZURE_ACCOUNT_KEY)
# BLOB_SERVICE_CLIENT = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)

# class EventsList(APIView):
#     def get(self, request, format=None):
#         events = Events.objects.all()
#         serializer = EventsSerializer(events, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         data = request.data.copy()  # Create a mutable copy of the QueryDict
#         data['category'] = 1  # Modify the category field

#         # Save the image and thumbnail to Azure Blob Storage and replace the datafield to the Azure link of the images
#         if 'image' in request.FILES:
#             image = request.FILES['image']
#             image_name = image.name

#             # Save the image to Azure Blob Storage
#             container_client = BLOB_SERVICE_CLIENT.get_container_client(AZURE_CONTAINER_NAME)
#             blob_client = container_client.get_blob_client(image_name)
#             blob_client.upload_blob(image.read(), overwrite=True)
#             image_url = f"https://{AZURE_ACCOUNT_NAME}.blob.core.windows.net/{AZURE_CONTAINER_NAME}/{image_name}"
#             data['image'] = image_url

#             # Create and save the thumbnail to Azure Blob Storage
#             thumb_io = BytesIO()
#             thumb_name = image_name.split('.')[0] + '_thumb.jpg'
#             image_file = Image.open(image)
#             image_file.thumbnail((300, 200))
#             image_file.save(thumb_io, 'JPEG', quality=85)
#             thumb_io.seek(0)

#             # Save the thumbnail to Azure Blob Storage
#             blob_client = container_client.get_blob_client(thumb_name)
#             blob_client.upload_blob(thumb_io.getvalue(), overwrite=True)
#             thumb_url = f"https://{AZURE_ACCOUNT_NAME}.blob.core.windows.net/{AZURE_CONTAINER_NAME}/{thumb_name}"
#             data['thumbnail'] = thumb_url

#         serializer = EventsSerializer(data=data)
#         if serializer.is_valid():
#             instance = serializer.save()
#             instance.slug = slugify(f"{instance.id}-{instance.name}")
#             instance.save()

#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# class EventsDetail(APIView):
#     def get_object(self, category_slug, events_slug):
#         try:
#             return Events.objects.filter(category__slug=category_slug).get(slug=events_slug)
#         except Events.DoesNotExist:
#             raise Http404
    
#     def get(self, request, category_slug, events_slug, format=None):
#         events = self.get_object(category_slug, events_slug)
#         serializer = EventsSerializer(events)
#         return Response(serializer.data)
        

# class EventsView(generics.RetrieveAPIView):
#     queryset = Events.objects.all()

#     def get(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         serializer = EventsSerializer(queryset, many=True)
#         return Response(serializer.data)


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
from django.core.files.storage import default_storage as storage

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
                storage.save(image_name, image)
                instance.image.name = image_name

            # Save the thumbnail file if it exists in the request.FILES dictionary
            if 'thumbnail' in request.FILES:
                thumbnail = request.FILES['thumbnail']
                thumbnail_name = f"{instance.slug}-thumbnail-{thumbnail.name}"
                storage.save(thumbnail_name, thumbnail)
                instance.thumbnail.name = thumbnail_name

            # Update the serializer with the generated slug
            serializer = EventsSerializer(instance)

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

