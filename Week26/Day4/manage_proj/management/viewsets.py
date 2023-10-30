from rest_framework import viewsets
from rest_framework.routers import DefaultRouter
from .models import Project, Task, Department, Employee
from .serializers import (
    ProjectSerializer,
    TaskSerializer,
    DepartmentSerializer,
    EmployeeSerializer,
)

router = DefaultRouter()


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


router.register("projects", ProjectViewSet, basename="projects")
router.register("tasks", TaskViewSet, basename="tasks")
router.register("departments", DepartmentViewSet, basename="departments")
router.register("employees", EmployeeViewSet, basename="employees")
