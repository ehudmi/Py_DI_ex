from django.core.management.base import BaseCommand
import requests
from faker import Faker
from random import randint
from gifs.models import Gif, Category

fake = Faker()


class Command(BaseCommand):
    help = "Populates the Gif model with data from the Giphy API"

    def handle(self, *args, **kwargs):
        API_URL = "https://api.giphy.com/v1/gifs/trending"
        API_KEY = "hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My"
        LIMIT = 20
        Faker.seed(1)

        response = requests.get(f"{API_URL}?limit={LIMIT}&rating=g&api_key={API_KEY}")
        if response.status_code != 200:
            self.stdout.write(self.style.ERROR("Failed to fetch data from Giphy API"))
            return
        response_json = response.json()
        Gif.objects.all().delete()
        images = response_json["data"]
        for image in images:
            title = image["title"]
            url = image["images"]["original"]["webp"]
            profile = fake.profile(["username"])
            gif = Gif(title=title, url=url, uploader_name=profile["username"])
            gif.save()
            cat_id = randint(1, Category.objects.all().count())
            gif.categories.add(Category.objects.filter(id=cat_id).first())
            if cat_id == 1:
                gif.categories.add(Category.objects.filter(id=cat_id + 1).first())
            else:
                gif.categories.add(Category.objects.filter(id=cat_id - 1).first())

        self.stdout.write(
            self.style.SUCCESS("Successfully populated and attributed gifs")
        )
