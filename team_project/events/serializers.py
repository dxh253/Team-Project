from rest_framework import serializers

from .models import Category, Events

class EventsSerializer(serializers.ModelSerializer):
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
        )
        
        
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

