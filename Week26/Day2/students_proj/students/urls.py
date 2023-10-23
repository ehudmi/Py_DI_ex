from django.urls import path
from .views import StudentListView, StudentDetailView

urlpatterns = [
    path("", StudentListView.as_view()),
    path("<int:pk>/", StudentDetailView.as_view()),
]
