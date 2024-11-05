from django.db import models
from django.contrib.auth.models import User

class Detection(models.Model):
    device_name = models.CharField(max_length=100)  # Name of the IoT device capturing the image
    location = models.CharField(max_length=255)     # Location where the image was captured
    image = models.ImageField(upload_to="detections/")  # Image file sent from the IoT device
    timestamp = models.DateTimeField(auto_now_add=True)  # Timestamp of when the image was captured
    detected = models.BooleanField(default=False)        # Whether a wild animal was detected
    confidence_score = models.FloatField(null=True, blank=True)  # Confidence score from the ML model
    species = models.CharField(max_length=100, null=True, blank=True)  # Species name, if identified

    def __str__(self):
        status = "Animal Detected" if self.detected else "No Animal Detected"
        return f"{status} - {self.device_name} at {self.timestamp}"


class Alert(models.Model):
    detection = models.ForeignKey(Detection, on_delete=models.CASCADE, related_name="alerts")
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Authorized user who triggered the alert
    timestamp = models.DateTimeField(auto_now_add=True)       # Time the alert was triggered
    resolved = models.BooleanField(default=False)             # Whether the alert has been resolved

    def __str__(self):
        return f"Alert for {self.detection} by {self.user.username} at {self.timestamp}"
