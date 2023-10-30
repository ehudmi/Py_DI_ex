from rest_framework import serializers
from .models import Project, Task, Department, Employee
from django.contrib.auth.models import User


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="project-detail", lookup_field="pk"
    )

    class Meta:
        model = Project
        fields = ["url", "name", "description", "start_date", "end_date"]


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="task-detail", lookup_field="pk"
    )

    class Meta:
        model = Task
        fields = ["url", "name", "description", "due_date", "completed", "project"]


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="department-detail",
        lookup_field="pk",
    )

    class Meta:
        model = Department
        fields = ["url", "name", "description", "admin"]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="user-detail",
        lookup_field="pk",
    )

    class Meta:
        model = User
        fields = ["url", "username", "email", "password"]


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="employee-detail", lookup_field="pk"
    )

    class Meta:
        model = Employee
        fields = ["url", "name", "email", "phone_number", "department", "projects"]


# class ProjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Project
#         fields = "__all__"


# class TaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Task
#         fields = "__all__"


# class DepartmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Department
#         fields = "__all__"


# class EmployeeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Employee
#         fields = "__all__"
