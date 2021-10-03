from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('db_service.urls')),
    path('',include('file_system.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
