from django.shortcuts import render, redirect
from .models import User, Card


def display_all_cards(request):
    context = {"cards": Card.objects.filter(current_owner_id=None)}
    return render(request, "cards/cards.html", context)


def display_one_card(request, card_id):
    context = {"card": Card.objects.filter(id=card_id).first()}
    return render(request, "cards/card_detail.html", context)


def user_profile(request, user_id):
    context = {
        "user": User.objects.filter(id=user_id).first(),
        "cards": Card.objects.filter(current_owner_id=user_id),
    }
    return render(request, "users/user_profile.html", context)


def buy_one_card(request, card_id, user_id):
    card = Card.objects.filter(id=card_id).first()
    user = User.objects.filter(id=user_id).first()
    if user is not None and card is not None:
        print(user.pk, card.pk)
        if user.amount_of_money >= card.price:
            card.previous_owner = card.current_owner
            card.current_owner = user
            user.amount_of_money -= card.price
            user.points += card.xp_points
        user.save()
        card.save()
    return redirect("homepage")


def sell_one_card(request, card_id, user_id):
    card = Card.objects.filter(id=card_id).first()
    user = User.objects.filter(id=user_id).first()
    if user is not None and card is not None:
        card.current_owner = None
        card.previous_owner = user
        user.amount_of_money += card.price
        user.points -= card.xp_points
        user.save()
        card.save()
    return redirect("homepage")
