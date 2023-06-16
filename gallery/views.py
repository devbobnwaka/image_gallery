from rest_framework.generics import ListCreateAPIView

from .models import Image
from .serializers import ImageSerializer

# Create your views here.

class ImageListCreateAPI(ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    