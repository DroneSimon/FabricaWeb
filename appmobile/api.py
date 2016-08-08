
from rest_framework_mongoengine import generics
from rest_framework import permissions

from .serializers import MobileDeviceSerializer
from .models import MobileDevice

class MobileDeviceList(generics.ListCreateAPIView):
    model = MobileDevice
    queryset = MobileDevice.objects.all()
    serializer_class = MobileDeviceSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class MobileDeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    model = MobileDevice
    queryset = MobileDevice.objects.all()
    serializer_class = MobileDeviceSerializer
    permission_classes = [
        permissions.AllowAny
    ]
