from django.core.management.base import BaseCommand
from countdown.models import Word
import os


class Command(BaseCommand):
    help = "Populates the Word model with data from the words.txt file"

    def handle(self, *args, **kwargs):
        Word.objects.all().delete()
        current_path = os.path.dirname(__file__)
        text = os.path.join(current_path, "sowpods.txt")

        with open(text) as f:
            for line in f:
                word_text = line.strip()
                word_length = len(word_text)
                category = "Random"
                word = Word(
                    word_text=word_text, word_length=word_length, category=category
                )
                word.save()

        self.stdout.write(
            self.style.SUCCESS("Successfully populated words from the words.txt file")
        )
