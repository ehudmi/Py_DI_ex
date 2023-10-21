from random import randint, sample
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .forms import WordGuessForm
from .models import HighScore, Word, Game


class CountdownGameView(FormView):
    template_name = "countdown/game.html"
    form_class = WordGuessForm
    success_url = reverse_lazy("game")

    def generate_word(self):
        self.words = Word.objects.filter(word_length__gte=6)
        word = self.words[randint(0, len(self.words) - 1)]
        shuffled = "".join(sample(word.word_text, word.word_length))
        Game.objects.filter(user=self.request.user).update(
            current_word=word.word_text, shuffled_word=shuffled, num_guesses=3
        )

    def get(self, request, *args, **kwargs):
        context = {}
        if self.request.user.is_authenticated:
            self.user_score, _ = HighScore.objects.get_or_create(
                player=self.request.user
            )
            self.game, _ = Game.objects.get_or_create(user=self.request.user)
        if self.game is not None:
            if self.game.num_guesses == 3 and self.game.current_word == "":
                self.generate_word()
            self.game = Game.objects.get(user=self.request.user)
        context["user_score"] = self.user_score
        context["game"] = self.game
        context["form"] = self.get_form()
        return render(self.request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {}
        self.game = Game.objects.get(user=self.request.user)
        self.words = Word.objects.filter(word_length__gte=6)
        self.user_score = HighScore.objects.get(player=self.request.user)
        form = self.get_form()
        if form.is_valid():
            guess = form.cleaned_data["guess"].upper()
            self.game.num_guesses -= 1
            if self.game is not None:
                if self.game.num_guesses == 0:
                    Game.objects.filter(user=self.request.user).update(
                        current_message="Game Over!",
                    )
                    self.generate_word()
                    self.game = Game.objects.get(user=self.request.user)
                    context["game"] = self.game
                    context["user_score"] = self.user_score
                    context["form"] = self.get_form()
                    return redirect("game")

            context["guess"] = guess
            if guess == self.game.current_word:
                self.game.current_message = "Perfect!"
                self.game.current_score += 10
            elif guess in self.words and len(guess) == len(self.game.current_word):
                self.game.current_message = "Excellent!"
                self.game.current_score += 8
            elif guess in self.words and len(guess) == len(self.game.current_word) - 1:
                self.game.current_message = "Good!"
                self.game.current_score += 5
            elif guess in self.words and len(guess) == len(self.game.current_word) - 2:
                self.game.current_message = "OK!"
                self.game.current_score += 3
            else:
                self.game.current_message = "Too Bad!"
        Game.objects.filter(user=self.request.user).update(
            num_guesses=self.game.num_guesses,
            current_score=self.game.current_score,
            current_message=self.game.current_message,
        )
        self.user_score.score += self.game.current_score

        HighScore.objects.filter(player=self.request.user).update(
            score=self.user_score.score
        )
        context["form"] = self.get_form()
        context["user_score"] = self.user_score
        context["game"] = self.game
        return redirect("game")
