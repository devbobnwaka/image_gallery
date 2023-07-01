from django.urls import path
from .views import ImageCreateAPIView, FilterImageAPI, ImageRetrieveUpdateAPIView, ImageListAPIView


urlpatterns = [
    path('filter-image/', FilterImageAPI.as_view(), name='filter-image'),
    path('image-create/', ImageCreateAPIView.as_view(), name='image-create'),
    path('image-list/', ImageListAPIView.as_view(), name='image-list'),
    path('image-retrieve-update/<slug:slug>/', ImageRetrieveUpdateAPIView.as_view(), name='image-retrieve-update'),
]
