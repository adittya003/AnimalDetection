# urls.py
from django.urls import path
from .views import RegisterUserView, LoginUserView, DetectionListCreate, DetectionRetrieveUpdateDestroy, DetectionFilterView, AlertListCreate

urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="register"),
    path("login/", LoginUserView.as_view(), name="login"),
    path("detections/", DetectionListCreate.as_view(), name="detection-list-create"),
    path("detections/<int:id>/", DetectionRetrieveUpdateDestroy.as_view(), name="detection-retrieve-update-destroy"),
    path("detections/filter/", DetectionFilterView.as_view(), name="detection-filter"),
    path("alerts/", AlertListCreate.as_view(), name="alert-list-create"),
]
