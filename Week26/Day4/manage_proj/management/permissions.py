from rest_framework import permissions
from .models import Department


class isDepartmentAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            department = Department.objects.filter(admin=request.user)
            if department:
                return True
            else:
                return False
