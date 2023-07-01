from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from authentication.authentication import BearerTokenAuthentication
from .models import Image
from .serializers import ImageSerializer, ListImageSerializer
from utils.utils import get_filtered_image
# Create your views here.

class ImageListAPIView(ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ListImageSerializer
    authentication_classes = [BearerTokenAuthentication]
    permission_classes = [IsAuthenticated]

class ImageCreateAPIView(CreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    authentication_classes = [BearerTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Image.objects.filter(user=user)

    
class ImageDetailAPIView(RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    lookup_field = 'slug'


class FilterImageAPI(APIView):
    def post(self, request, format=None):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            image_file = serializer.validated_data['image_path']
            print(image_file)
            action = serializer.validated_data['action']
            filter_img = get_filtered_image(image_file, action)
            return Response({"filtered_img": filter_img})
        return Response(serializer.errors)
    