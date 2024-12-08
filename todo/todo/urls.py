from core.views import Custom403View, Custom404View, Custom500View
from django.contrib import admin
from django.urls import include, path

handler404 = Custom404View.as_view()
handler403 = Custom403View.as_view()
handler500 = Custom500View.as_view()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
    path('accounts/', include('users.urls')),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
