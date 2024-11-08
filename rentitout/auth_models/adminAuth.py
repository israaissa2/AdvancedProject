from rest_framework.permissions import BasePermission


class AdminAuth(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == 2:
            return True
        return False
