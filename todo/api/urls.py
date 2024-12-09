from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import RegisterViewSet, TaskViewSet

app_name = 'api'

v1_router = DefaultRouter()

v1_router.register(r'tasks', TaskViewSet, basename='task')
v1_router.register(r'users', RegisterViewSet, basename='users')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
