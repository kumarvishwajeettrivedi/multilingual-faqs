from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    """Allow only admins to edit, others can only read."""
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return request.user.is_staff
