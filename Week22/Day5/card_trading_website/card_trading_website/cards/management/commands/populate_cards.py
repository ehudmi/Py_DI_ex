from django.core.management.base import BaseCommand
import requests
from random import randint
from datetime import datetime
from cards.models import Card


class Command(BaseCommand):
    help = "Populates the Card model with data from the Harry Potter API"

    def handle(self, *args, **kwargs):
        API_URL = "https://hp-api.onrender.com/api/characters"
        response = requests.get(API_URL)
        if response.status_code != 200:
            self.stdout.write(
                self.style.ERROR("Failed to fetch data from Harry Potter API")
            )
            return

        characters = response.json()

        Card.objects.all().delete()

        for character in characters:
            id = character.get("id", "")
            name_character = character.get("name", "")
            species = character.get("species", "")
            house = character.get("house", "")
            image_url = character.get("image", "")
            date_of_birth = character.get("dateOfBirth", "")
            patronus = character.get("patronus", "")
            price = randint(200, 2000)
            xp_points = randint(1, 10)
            current_owner = None
            previous_owner = None

            if date_of_birth:
                date_of_birth = datetime.strptime(date_of_birth, "%d-%m-%Y").strftime(
                    "%Y-%m-%d"
                )

            card = Card(
                id,
                name_character,
                species,
                house,
                image_url,
                date_of_birth,
                patronus,
                price,
                xp_points,
                current_owner,
                previous_owner,
            )
            card.save()

        self.stdout.write(
            self.style.SUCCESS("Successfully populated cards from the Harry Potter API")
        )
