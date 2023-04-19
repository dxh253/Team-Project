from rest_framework import serializers

from .models import Problems



class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problems
        fields = (
            "id",
            "title",
            "description",
            "date_added",
            "user"
        )

    def create(self, validated_data):
        problem = Problems.objects.create(**validated_data)
        return problem