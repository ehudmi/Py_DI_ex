from django.urls import path
from . import views

urlpatterns = [
    path("add_todo/", views.add_todo, name="add-todo"),
    path("todo_done/<todo_id>/", views.todo_done, name="todo-done"),
    path("<category_name>/", views.show_by_category, name="list-category"),
]
