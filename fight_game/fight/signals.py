from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Figure, FigureImage, Battle, FightUser


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


@receiver(pre_delete, sender=Battle)
def update_results(sender, **kwargs):
    battle = Battle.objects.all().order_by("-score").first()
    if battle is not None and battle.player is not None and battle.figure is not None:
        figure = Figure.objects.get(id=battle.figure.pk)
        figure.luck += 1
        winner = FightUser.objects.get(id=battle.player.pk)
        winner.figures_played.add(figure)
        winner.matches_played += 1
        winner.matches_won += 1
        winner.save()
    else:
        battle = Battle.objects.all().order_by("-score").last()
        if (
            battle is not None
            and battle.player is not None
            and battle.figure is not None
        ):
            figure = Figure.objects.get(id=battle.figure.pk)
            figure.luck -= 1
            loser = FightUser.objects.get(id=battle.player.pk)
            loser.figures_played.add(figure)
            loser.matches_played += 1
            loser.save()
