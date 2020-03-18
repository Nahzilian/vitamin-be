from .models import Guest
from rest_framework import viewsets, permissions
from .serializers import GuestSerializer

#Guest viewset

class GuestViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]

    serializer_class = GuestSerializer