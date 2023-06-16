from django.urls import path
from .views import EmailAuthToken, LogOutViewAPI, RegisterUserAPI, UserRetrieveUpdateAPI

urlpatterns = [
    path('login/', EmailAuthToken.as_view(), name='login'),
    path('logout/', LogOutViewAPI.as_view(), name='logout'),
    path('register/', RegisterUserAPI.as_view(), name='register'),
    path('<int:pk>/retrieve-detail/', UserRetrieveUpdateAPI.as_view(), name='retrieve-detail'),
]
