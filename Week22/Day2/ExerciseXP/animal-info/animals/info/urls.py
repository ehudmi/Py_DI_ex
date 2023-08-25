from django.urls import path

# from .views import (
#     display_all_animals,
#     display_all_families,
#     display_animal_per_family,
#     display_one_animal,
# )
from . import views

urlpatterns = [
    path("animals/", views.display_all_animals),
    path("families/", views.display_all_families),
    path("animal_in_family/<int:family_id>/", views.display_animal_per_family),
    path("animal/<int:animal_id>/", views.display_one_animal),
]
