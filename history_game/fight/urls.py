from django.urls import path
from . import views

urlpatterns = [path("", views.index), path("get_figure", views.get_figure)]
