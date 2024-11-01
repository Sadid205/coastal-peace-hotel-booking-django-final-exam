from rest_framework import viewsets
from .models import Banner
from .serializers import BannerSerializer
from rest_framework import permissions
# Create your views here.


class BannerView(viewsets.ModelViewSet):
    permission_classes=[permissions.IsAuthenticated]
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer