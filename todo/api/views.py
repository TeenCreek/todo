from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import AllowAny, IsAuthenticated
from tasks.models import Task

from .serializers import RegisterSerializer, TaskSerializer, UserSerializer

User = get_user_model()


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('is_completed',)
    search_fields = ('title',)

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        task = self.get_object()

        if task.author != self.request.user:
            raise PermissionDenied('Вы не можете изменять эту задачу')

        serializer.save()

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Вы не можете удалить эту задачу')

        instance.delete()


class RegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return RegisterSerializer

        return UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            return (AllowAny(),)

        return (IsAuthenticated(),)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return User.objects.filter(pk=self.request.user.id)

        return User.objects.none()
