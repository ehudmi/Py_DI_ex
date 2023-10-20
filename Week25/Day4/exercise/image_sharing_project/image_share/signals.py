from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Profile, Image, Follow


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


@receiver(post_save, sender=Follow)
def update_number_following(sender, **kwargs):
    if kwargs["created"]:
        profile = Profile.objects.get(user=kwargs["instance"].follower)
        profile.number_following += 1
        profile.save()


@receiver(post_delete, sender=Follow)
def update_number_following_delete(sender, **kwargs):
    profile = Profile.objects.get(user=kwargs["instance"].follower)
    profile.number_following -= 1
    profile.save()
