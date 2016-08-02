
from rest_framework_mongoengine import serializers

from .models import MobileDevice

class MobileDeviceSerializer(serializers.DocumentSerializer):
    class Meta:
        model = MobileDevice

