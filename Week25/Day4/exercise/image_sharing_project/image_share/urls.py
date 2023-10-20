from django.urls import path
from .views import (
    IndexView,
    UploadImageView,
    MyImagesView,
    CreateAlbumView,
    AlbumView,
    FeedView,
    SetFollowView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("upload/", UploadImageView.as_view(), name="upload_image"),
    path("my_images/", MyImagesView.as_view(), name="my_images"),
    path("create_album/", CreateAlbumView.as_view(), name="create_album"),
    path("album/<int:pk>/", AlbumView.as_view(), name="view_album"),
    path("feed/", FeedView.as_view(), name="feed"),
    path("set_follow/<int:pk>/", SetFollowView.as_view(), name="set_follow"),
]
