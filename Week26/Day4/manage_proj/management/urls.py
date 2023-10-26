from django.urls import path
from .views import ProjectAPIView, TaskAPIView, DepartmentAPIView, EmployeeAPIView

urlpatterns = [
    path("projects/", ProjectAPIView.as_view(), name="project-operations"),
    path("tasks/", TaskAPIView.as_view(), name="task-operations"),
    path("departments/", DepartmentAPIView.as_view(), name="department-operations"),
    path("employees/", EmployeeAPIView.as_view(), name="employee-operations"),
]
