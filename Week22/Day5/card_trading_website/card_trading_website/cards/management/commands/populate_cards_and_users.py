from django.core.management.base import BaseCommand
from faker import Faker
from random import randint
from cards.models import User, Card

fake = Faker()


class Command(BaseCommand):
    help = "Populates the users with fake data and attribute cards"

    def handle(self, *args, **kwargs):
        User.objects.all().delete()

        Faker.seed(1)
        for _ in range(11):
            profile = fake.profile(["username", "mail"])
            user_id = User.objects.all().count() + 1
            user = User(user_id, profile["username"], profile["mail"], 1000, 0)
            user.save()
            cards = Card.objects.filter(price__lt=1000)
            for _ in range(0, randint(0, 5)):
                card_index = randint(0, len(cards))
                if user.amount_of_money >= cards[card_index].price:
                    cards[card_index].previous_owner = cards[card_index].current_owner
                    previous = cards[card_index].previous_owner
                    if previous is not None:
                        previous.amount_of_money += cards[card_index].price
                        previous.points -= cards[card_index].xp_points
                        previous.save()

                    cards[card_index].current_owner = user
                    user.amount_of_money -= cards[card_index].price
                    user.points += cards[card_index].xp_points
                    cards[card_index].save()
                    user.save()

        self.stdout.write(
            self.style.SUCCESS("Successfully populated users and attributed cards")
        )
