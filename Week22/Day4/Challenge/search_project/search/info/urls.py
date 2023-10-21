from django.urls import path
from . import views

urlpatterns = [
    path("person/phonenumber/<str:number>", views.display_person_by_phonenumber),
    path("person/name/<str:name>", views.display_person_by_name),
]
