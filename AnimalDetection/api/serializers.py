from rest_framework import serializers
from .models import Detection, Alert

class DetectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detection
        fields = ["id", "device_name", "location", "image", "timestamp", "detected", "confidence_score", "species"]

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ["id", "detection", "user", "timestamp", "resolved"]
