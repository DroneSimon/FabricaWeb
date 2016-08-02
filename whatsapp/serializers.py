
from rest_framework_mongoengine import serializers

from .models import WhatsappReceived

class WhatsappReceivedSerializer(serializers.DocumentSerializer):
    class Meta:
        model = WhatsappReceived

