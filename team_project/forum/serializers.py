from rest_framework import serializers

from .models import Forum, Thread, Post

from django.conf import settings

class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = '__all__'

class ThreadSerializer(serializers.ModelSerializer):
    get_image = serializers.ImageField(max_length=None, use_url=True, required=False)
    get_thumbnail = serializers.ImageField(max_length=None, use_url=True, required=False)
    author_name = serializers.CharField(source='author.username', read_only=True)
    forum_name = serializers.CharField(source='forum.name', read_only=True)
    posts = serializers.SerializerMethodField()

    class Meta:
        model = Thread
        fields = (
            "id",
            "forum",
            "forum_name",
            "author",
            "author_name",
            "title",
            "content",
            "date_added",
            "upvotes",
            "downvotes",
            "score",
            "get_image",
            "get_thumbnail",
            "posts",
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
    
    def get_posts(self, obj):
        posts = Post.objects.filter(thread=obj)
        serializer = PostSerializer(posts, many=True)
        return serializer.data
    
class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)
    thread_title = serializers.CharField(source='thread.title', read_only=True)
    thread_forum = serializers.CharField(source='thread.forum.name', read_only=True)
    
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