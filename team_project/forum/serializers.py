from rest_framework import serializers

from .models import Category, Thread, Post

from django.conf import settings

class ThreadSerializer(serializers.ModelSerializer):
    get_image = serializers.ImageField(max_length=None, use_url=True, required=False)
    get_thumbnail = serializers.ImageField(max_length=None, use_url=True, required=False)

    class Meta:
        model = Thread
        fields = (
            "id",
            "title",
            "get_absolute_url",
            "description",
            "venue",
            "date_added",
            "get_image",
            "get_thumbnail",
            "category",
            "slug",
            "author",
            "score",
        )

    def create(self, validated_data):
        image = validated_data.pop('get_image', None)
        thumbnail = validated_data.pop('get_thumbnail', None)
        thread = Thread.objects.create(**validated_data)
        if image:
            thread.image = image
        if thumbnail:
            thread.thumbnail = thumbnail
        thread.save()
        return thread

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.image:
            representation['get_image'] = f"{settings.BASE_URL}{instance.image.url}"
        if instance.thumbnail:
            representation['get_thumbnail'] = f"{settings.BASE_URL}{instance.thumbnail.url}"
        return representation
    
class CategorySerializer(serializers.ModelSerializer):
    threads = ThreadSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "threads",
        )

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "thread",
            "author",
            "content",
            "date_added",
            "upvotes",
            "downvotes",
        )