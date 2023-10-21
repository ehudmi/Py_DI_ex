from django.contrib import admin
from django.urls import path, include
from .views import RegisterView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("book_app.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/register/", RegisterView.as_view(), name="register"),
]
