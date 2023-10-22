from django.contrib import admin
from django.urls import path, include
from posts.views import PostMixinListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/posts/", PostMixinListView.as_view(), name="post-list"),
]
