from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    CreateAPIView,
)
from .models import Project, Task, Department, Employee
from .serializers import (
    ProjectSerializer,
    TaskSerializer,
    DepartmentSerializer,
    EmployeeSerializer,
)


class ProjectAPIView(ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TaskAPIView(ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class DepartmentAPIView(ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeeAPIView(ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
