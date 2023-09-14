from django.shortcuts import render, redirect
from .forms import ToDoForm
from .models import Todo


def add_todo(request):
    context = {"todos": Todo.objects.all()}
    if request.method == "POST":
        form = ToDoForm(request.POST)
        print(form.data["date_creation"])
        if form.is_valid():
            form.save()
            return redirect("add-todo")
    else:
        form = ToDoForm()
    context["form"] = form
    return render(request, "todos/tasks_list.html", context)
