from rest_framework import serializers

from .models import Category, Events

from django.conf import settings

from django.core.files.base import ContentFile
from azure.storage.blob import BlobServiceClient
from io import BytesIO
from django.utils.text import slugify
import os

AZURE_ACCOUNT_NAME = getattr(settings, 'AZURE_ACCOUNT_NAME', '')
AZURE_ACCOUNT_KEY = getattr(settings, 'AZURE_ACCOUNT_KEY', '')
AZURE_CONTAINER_NAME = getattr(settings, 'AZURE_CONTAINER_NAME', '')

AZURE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=%s;AccountKey=%s;EndpointSuffix=core.windows.net" % (AZURE_ACCOUNT_NAME, AZURE_ACCOUNT_KEY)
BLOB_SERVICE_CLIENT = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
    
    
class EventsSerializer(serializers.ModelSerializer):
    get_image = serializers.ImageField(max_length=None, use_url=True, required=False)
    get_thumbnail = serializers.ImageField(max_length=None, use_url=True, required=False)
    class Meta:
        model = Events
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "venue",
            "date",
            "get_image",
            "get_thumbnail",
            "category",
            "slug"
        )


    def create(self, validated_data):
        image = validated_data.pop('get_image', None)
        thumbnail = validated_data.pop('get_thumbnail', None)
        event = Events.objects.create(image=image, thumbnail=thumbnail, **validated_data)
        return event

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.image and instance.image.storage.exists(instance.image.name):
            representation['get_image'] = instance.image.url
        if instance.thumbnail and instance.thumbnail.storage.exists(instance.thumbnail.name):
            representation['get_thumbnail'] = instance.thumbnail.url
        return representation


class CategorySerializer(serializers.ModelSerializer):
    events = EventsSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "events",
        )