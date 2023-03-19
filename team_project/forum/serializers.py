from rest_framework import serializers
from .models import Subreddit, Post, PostVotes

from django.contrib.auth.models import User

from django.contrib.auth import get_user_model

class SubredditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subreddit
        fields = (
            "id",
            "name",
            "description",
            "slug"
        )

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "content",
            "subreddit",
            "author",
            "slug"
        )
    
class PostVotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostVotes
        fields = (
            "id",
            "post",
            "user",
            "vote"
        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "username",
            "email",
            "password"
        )
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user
    
