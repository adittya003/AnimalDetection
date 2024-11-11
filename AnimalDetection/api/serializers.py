# serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Detection, Alert

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("id", "username", "password")

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"]
        )
        return user

class DetectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detection
        fields = ["id", "device_name", "location", "image", "timestamp", "detected", "confidence_score", "species", "dangerous"]

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ["id", "detection", "user", "timestamp", "resolved"]
