from django.urls import path

from .views import AuthApiRootView, RegisterView


urlpatterns = [
    path("", AuthApiRootView.as_view(), name="auth-api-root"),
    path("register", RegisterView.as_view(), name="register"),
]

