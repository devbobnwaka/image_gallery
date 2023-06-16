from django.urls import path
from .views import ImageListCreateAPI


urlpatterns = [
    path('gallery/', ImageListCreateAPI.as_view(), name='list-create'),
]
