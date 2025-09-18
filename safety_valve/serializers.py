from .models import SafetyValve
from rest_framework import serializers

class SafetyValveSerializer(serializers.ModelSerializer):
    class Meta:
        model = SafetyValve
        fields = ['description', 'tag', 'manufacturer', 'serial_number', 'model', 'size', 'actuation_range']