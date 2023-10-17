from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile, Image


@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    if kwargs["created"]:
        Profile.objects.create(user=kwargs["instance"])


@receiver(post_save, sender=Image)
def update_number_images_uploaded(sender, **kwargs):
    if kwargs["created"]:
        profile = Profile.objects.get(user=kwargs["instance"].author)
        profile.number_images_uploaded += 1
        profile.save()
