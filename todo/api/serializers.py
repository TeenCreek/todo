from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from tasks.models import Task

User = get_user_model()


class TaskSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'description',
            'is_completed',
            'created_at',
            'updated_at',
            'author',
        )


# class TaskCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Task
#         fields = ('title', 'description', 'is_completed')


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ('username', 'email', 'password')
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(), fields=['username', 'email']
            )
        ]
