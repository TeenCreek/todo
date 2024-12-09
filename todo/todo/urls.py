from core.views import Custom403View, Custom404View, Custom500View
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="ToDo",
        default_version='v1',
        description="ToDo Проект",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


handler404 = Custom404View.as_view()
handler403 = Custom403View.as_view()
handler500 = Custom500View.as_view()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
    path('accounts/', include('users.urls')),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path(
        'swagger<format>/',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json',
    ),
    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui',
    ),
    path(
        'redoc/',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc',
    ),
]
