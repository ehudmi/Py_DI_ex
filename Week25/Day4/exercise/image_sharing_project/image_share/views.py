from .models import Image, Profile
from .forms import ImageForm
from django.views.generic import ListView, CreateView


class IndexView(ListView):
    model = Image
    template_name = "image_share/index.html"
    context_object_name = "images"


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
