from django.urls import path

from .views import (
    ProjectAPIView,
    TaskAPIView,
    DepartmentAPIView,
    EmployeeAPIView,
    TaskDetailAPIView,
    ProjectDetailAPIView,
    DepartmentDetailAPIView,
    EmployeeDetailAPIView,
    UserAPIView,
    UserDetailAPIView,
)


urlpatterns = [
    path("projects/", ProjectAPIView.as_view(), name="project-operations"),
    path("projects/<int:pk>/", ProjectDetailAPIView.as_view(), name="project-detail"),
    path("tasks/", TaskAPIView.as_view(), name="task-operations"),
    path("tasks/<int:pk>/", TaskDetailAPIView.as_view(), name="task-detail"),
    path("departments/", DepartmentAPIView.as_view(), name="department-operations"),
    path(
        "departments/<int:pk>/",
        DepartmentDetailAPIView.as_view(),
        name="department-detail",
    ),
    path("employees/", EmployeeAPIView.as_view(), name="employee-operations"),
    path(
        "employees/<int:pk>/",
        EmployeeDetailAPIView.as_view(),
        name="employee-detail",
    ),
    path("users/", UserAPIView.as_view(), name="user-operations"),
    path(
        "users/<int:pk>/",
        UserDetailAPIView.as_view(),
        name="user-detail",
    ),
]
