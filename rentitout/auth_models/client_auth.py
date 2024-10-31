from rest_framework.permissions import BasePermission


class IsClient(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == 1:
            return True
        else:
            return False
