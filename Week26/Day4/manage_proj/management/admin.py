from django.contrib import admin
from .models import Project, Task, Department, Employee

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Department)
admin.site.register(Employee)
