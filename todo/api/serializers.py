from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
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


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=(validate_password,)
    )
    email = serializers.EmailField(
        required=True,
        validators=(
            UniqueValidator(
                queryset=User.objects.all(),
                message='Пользователь с таким e-mail уже существует',
            ),
        ),
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
