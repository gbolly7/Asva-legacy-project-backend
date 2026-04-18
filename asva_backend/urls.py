from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include("accounts.urls")),
    path("api/me/", include("accounts.me_urls")),
    path("api/payments/", include("payments.urls")),
    path("api/admin/", include("payments.admin_urls")),
    path("api/cms/", include("cms.urls")),
]

