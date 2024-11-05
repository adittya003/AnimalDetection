from django.urls import path
from . import views

urlpatterns = [
    path("detections/", views.DetectionListCreate.as_view(), name="detection-list-create"),
    path("detections/<int:id>/", views.DetectionRetrieveUpdateDestroy.as_view(), name="detection-retrieve-update-destroy"),
    path("detections/filter/", views.DetectionFilterView.as_view(), name="detection-filter"),
    path("alerts/", views.AlertListCreate.as_view(), name="alert-list-create"),
]
