from django.urls import path
from .views import EmailAuthToken, LogOutViewAPI

urlpatterns = [
    path('login/', EmailAuthToken.as_view(), name='login'),
    path('logout/', LogOutViewAPI.as_view(), name='logout')
]
