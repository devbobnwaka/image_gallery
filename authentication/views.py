from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .authentication import BearerAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class EmailAuthToken(APIView):
    def post(self, request, *args, **kwargs):
        email = self.request.data.get('email')
        password = self.request.data.get('password')
        if email and password:
            user = authenticate(request, email=email, password=password)
            if user is not None:
                # A backend authenticated the credentials
                token, created = Token.objects.get_or_create(user=user)
                return Response({
                    'token': token.key,
                    'user_id': user.pk,
                    'email': user.email
                })
            else:
            # No backend authenticated the credentials
                return Response({'error': 'Incorrect username or password'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class LogOutViewAPI(APIView):
    authentication_classes = [BearerAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        token = request.auth
        Token.objects.filter(key=token).delete()
        return Response({"message":"Logout successfully"})