from django.shortcuts import render
from .forms import ToDoForm


def add_todo(request):
    context = {}
    context["page_title"] = "Add Todo"
    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid():
            form_title = form.cleaned_data(["title"])
            form_details = form.cleaned_data(["details"])
            form_has_been_done = form.cleaned_data(["has_been_done"])
            form_date_creation = form.cleaned_data(["date_creation"])
            form_date_completion = form.cleaned_data(["date_completion"])
            form_deadline_date = form.cleaned_data(["deadline_date"])
            context["formInfo"] = {
                "title": form_title,
                "details": form_details,
                "has_been_done": form_has_been_done,
                "date_creation": form_date_creation,
                "date_completion": form_date_completion,
                "deadline_date": form_deadline_date,
            }
            print(context["formInfo"])
            return render(request, "todos/tasks_list.html", context)
        else:
            print("---ERRORS---", form.errors)
            context["form"] = form
            return render(request, "todos/tasks_list.html", context)
    else:
        context["form"] = ToDoForm()
        return render(request, "todos/tasks_list.html", context)
