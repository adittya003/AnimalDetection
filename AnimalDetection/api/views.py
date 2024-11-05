from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Detection, Alert
from .serializers import DetectionSerializer, AlertSerializer


class DetectionListCreate(generics.ListCreateAPIView):
    queryset = Detection.objects.all()
    serializer_class = DetectionSerializer


class DetectionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Detection.objects.all()
    serializer_class = DetectionSerializer
    lookup_field = "id"


class DetectionFilterView(APIView):
    def get(self, request, species=None, location=None):
        detections = Detection.objects.all()
        if species:
            detections = detections.filter(species=species)
        if location:
            detections = detections.filter(location=location)
        serializer = DetectionSerializer(detections, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DetectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None):
        detection = get_object_or_404(Detection, id=id)
        serializer = DetectionSerializer(detection, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        detection = get_object_or_404(Detection, id=id)
        detection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AlertListCreate(generics.ListCreateAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
