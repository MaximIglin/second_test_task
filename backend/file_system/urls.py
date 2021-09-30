from django.urls import path
from .views import AddToFileApi, AddImageApi


urlpatterns = [
    path('api/file_system/', AddToFileApi.as_view()),
    path('api/images/', AddImageApi.as_view())
]