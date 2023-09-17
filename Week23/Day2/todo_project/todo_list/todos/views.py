from django.shortcuts import render, redirect, get_object_or_404
import datetime
from .forms import ToDoForm
from .models import Todo


def add_todo(request):
    context = {}
    context["todos"] = Todo.objects.all()
    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add-todo")
    else:
        form = ToDoForm()
    context["form"] = form
    return render(request, "todos/tasks_list.html", context)


def todo_done(request, todo_id):
    task = get_object_or_404(Todo, id=todo_id)
    task.has_been_done = True
    task.date_completion = datetime.date.today()
    task.save()
    return redirect("add-todo")


def show_by_category(request, category_name):
    todos = Todo.objects.filter(category__name=category_name)
    print(todos[0])
    # todos = get_object_or_404(Todo, category__name=category_name)
    context = {"category": category_name, "todos": todos}
    return render(request, "todos/list_by_category.html", context)
