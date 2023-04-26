from rest_framework import serializers

from .models import Problems, Comment


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problems
        fields = (
            "id",
            "title",
            "description",
            "date_added",
            "owner",
            "author",
        )

    def create(self, validated_data):
        problem = Problems.objects.create(**validated_data)
        return problem


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "id",
            "problem",
            "text",
            "created_date",
            "date",
            "author",
            "username",
        )

    def create(self, validated_data):
        return super().create(validated_data)
