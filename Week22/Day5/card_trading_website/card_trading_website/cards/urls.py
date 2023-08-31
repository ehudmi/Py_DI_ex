from django.urls import path
from . import views

urlpatterns = [
    path("", views.display_all_cards, name="homepage"),
    path("cards/<card_id>/", views.display_one_card, name="card-detail"),
    path("users/<user_id>/", views.user_profile, name="user-profile"),
    path("cards/<card_id>/buy/<user_id>/", views.buy_one_card, name="buy-card"),
    path("cards/<card_id>/sell/<user_id>/", views.sell_one_card, name="sell-card"),
]
