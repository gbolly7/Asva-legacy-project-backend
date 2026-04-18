from django.urls import path

from .views import (
    AdminConfirmPaymentView,
    AdminNotificationReadView,
    AdminNotificationsView,
    AdminPaymentClaimsView,
    AdminRejectPaymentView,
)


urlpatterns = [
    path("payment-claims", AdminPaymentClaimsView.as_view(), name="admin-payment-claims"),
    path("payment-claims/<int:pk>/confirm", AdminConfirmPaymentView.as_view(), name="admin-payment-confirm"),
    path("payment-claims/<int:pk>/reject", AdminRejectPaymentView.as_view(), name="admin-payment-reject"),
    path("notifications", AdminNotificationsView.as_view(), name="admin-notifications"),
    path("notifications/<int:pk>/read", AdminNotificationReadView.as_view(), name="admin-notification-read"),
]
