from django.urls import path

from .views import PublicContentView


urlpatterns = [
    path("content/<slug:slug>", PublicContentView.as_view(), name="cms-content-detail"),
]

