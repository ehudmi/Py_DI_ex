from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Figure, FigureImage, Battle


@receiver(post_save, sender=FigureImage)
def update_number_images(sender, **kwargs):
    if kwargs["created"]:
        figure = Figure.objects.get(name=kwargs["instance"].figure)
        figure.num_images += 1
        figure.save()


@receiver(post_save, sender=Battle)
def update_figure_attributes(sender, **kwargs):
    if kwargs["created"]:
        figure = Figure.objects.get(name=kwargs["instance"].figure)
        figure.notoriety += 1
        figure.save()
