import os
import pygame
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from .models import Detection, Alert
from .serializers import DetectionSerializer, AlertSerializer, UserSerializer

# Initialize Pygame mixer for playing sounds
pygame.mixer.init()

# Register User View
class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # Allow access to registration without authentication

# Login User View
class LoginUserView(APIView):
    permission_classes = [AllowAny]  # Allow access to login without authentication

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

# Detection List and Create View
class DetectionListCreate(generics.ListCreateAPIView):
    queryset = Detection.objects.all()
    serializer_class = DetectionSerializer

# Detection Retrieve, Update and Destroy View
class DetectionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Detection.objects.all()
    serializer_class = DetectionSerializer
    lookup_field = "id"

# Detection Filter View
class DetectionFilterView(APIView):
    def post(self, request):
        dangerous = request.data.get("dangerous", False)
        if dangerous:
            # Debugging log to see the flow
            print("Dangerous animal detected, trying to play alert sound...")

            # Try to load and play alert.mp3 with an absolute path
            try:

                # Play the sound
                pygame.mixer.music.load("/home/shahin/Documents/AnimalDetectionAPI/AnimalDetection/AnimalDetection/api/sound/lion_roaring_gry-236748.mp3")
                pygame.mixer.music.play()
                print("Alert sound played successfully.")
                return Response({"status": "Alert sound played for dangerous animal"}, status=status.HTTP_200_OK)

            except pygame.error as e:
                print(f"Error while playing sound: {str(e)}")
                return Response({"error": f"Error while playing sound: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({"status": "No dangerous animal detected"}, status=status.HTTP_200_OK)

# Alert List and Create View
class AlertListCreate(generics.ListCreateAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
