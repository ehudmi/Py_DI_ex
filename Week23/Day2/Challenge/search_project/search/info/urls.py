from django.urls import path
from . import views

urlpatterns = [
    path(
        "person/phonenumber/<number>", views.display_person_by_phonenumber, name="phone"
    ),
    path("person/name/<name>", views.display_person_by_name, name="person"),
    path("person/add_person", views.add_person, name="add-person"),
]
