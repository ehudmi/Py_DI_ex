from django.urls import path
from .views import IndexView, UploadImageView, MyImagesView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("upload/", UploadImageView.as_view(), name="upload_image"),
    path("my_images/", MyImagesView.as_view(), name="my_images"),
]
