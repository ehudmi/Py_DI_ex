from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User
from .models import Image, Profile, Album, Follow
from .forms import ImageForm
from django.views.generic import ListView, CreateView, View


class IndexView(ListView):
    model = Image
    template_name = "image_share/index.html"
    context_object_name = "data"

    def get_queryset(self):
        context = {}
        context["images"] = Image.objects.all()
        context["albums"] = Album.objects.all()
        context["follow"] = Follow.objects.filter(
            follower=self.request.user
        ).values_list("following", flat=True)
        return context


class UploadImageView(CreateView):
    model = Image
    template_name = "image_share/upload_image.html"
    form_class = ImageForm
    success_url = "/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class MyImagesView(ListView):
    model = Image
    template_name = "image_share/my_images.html"
    context_object_name = "data"

    def get_queryset(self):
        context = {}
        context["images"] = Image.objects.filter(author=self.request.user)
        context["profile"] = Profile.objects.get(user=self.request.user)
        return context


class CreateAlbumView(CreateView):
    model = Album
    template_name = "image_share/create_album.html"
    fields = ["title", "description"]
    success_url = "/"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class AlbumView(ListView):
    model = Album
    template_name = "image_share/view_albums.html"
    context_object_name = "data"

    def get_queryset(self):
        context = {}
        context["images"] = Image.objects.filter(album=self.kwargs["pk"])
        context["album"] = Album.objects.get(id=self.kwargs["pk"])
        return context


class SetFollowView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = User.objects.get(pk=self.kwargs["pk"])
            if Follow.objects.filter(follower=request.user, following=user).exists():
                Follow.objects.get(follower=request.user, following=user).delete()
            else:
                Follow.objects.create(follower=request.user, following=user)
            return redirect("index")
        else:
            return HttpResponseForbidden()


class FeedView(ListView):
    model = Image
    template_name = "image_share/feed.html"
    context_object_name = "data"

    def get_queryset(self):
        context = {}
        following = Follow.objects.filter(follower=self.request.user)
        context["images"] = Image.objects.filter(
            author__in=following.values("following")
        )
        context["albums"] = Album.objects.filter(
            created_by__in=following.values("following")
        )
        context["follow"] = Follow.objects.filter(
            follower=self.request.user
        ).values_list("following", flat=True)
        context["count_follow"] = Profile.objects.get(user=self.request.user)
        return context
