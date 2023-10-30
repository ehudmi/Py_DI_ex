from django.contrib import admin
from django.urls import path, include
from management.viewsets import router

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("", include("management.urls")),
    # path("", include(router.urls)),
]
