from django.urls import path

from .views import ReferenceView


urlpatterns = [
    path("reference", ReferenceView.as_view(), name="me-reference"),
]
