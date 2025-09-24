from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdmin(BasePermission):
    """
    Permite acceso solo a usuarios con rol administrador (id_role=3).
    """
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.id_role == 3)


class IsTeacherOrAdmin(BasePermission):
    """
    Permite acceso solo a profesores (id_role=2) o admins (id_role=3).
    """
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.id_role in [2, 3])


class ReadOnlyOrTeacherOrAdmin(BasePermission):
    """
    Permite solo lectura a estudiantes (id_role=1).
    Profesores y admins pueden hacer todo.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated
        return request.user.is_authenticated and request.user.id_role in [2, 3]
