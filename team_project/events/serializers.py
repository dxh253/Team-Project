from rest_framework import serializers

from .models import Category, Events

from django.conf import settings

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
        event = Events.objects.create(**validated_data)
        if image:
            event.image = image
        if thumbnail:
            event.thumbnail = thumbnail
        event.save()
        return event

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.image:
            representation['get_image'] = f"{settings.SERVER_URL}{instance.image.url}"
        if instance.thumbnail:
            representation['get_thumbnail'] = f"{settings.SERVER_URL}{instance.thumbnail.url}"
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

