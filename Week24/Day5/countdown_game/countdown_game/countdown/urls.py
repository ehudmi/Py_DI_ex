from django.urls import path
from .views import CountdownGameView

urlpatterns = [path("game/", CountdownGameView.as_view(), name="game")]
