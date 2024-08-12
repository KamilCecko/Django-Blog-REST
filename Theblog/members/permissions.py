from rest_framework.permissions import BasePermission


class IsSuperUserOrStaff(BasePermission):
    def has_permission(self, request, view):
        return (
                request.user.is_authenticated and
                (request.user.is_superuser or request.user.is_staff)
            )


class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        elif request.method in ['POST']:
            if request.user.is_authenticated:
                return True
        elif request.method in ['PUT', 'DELETE']:
            if (request.user.is_superuser or
                    request.user.is_staff or
                    request.user == view.get_object().author):
                return True
        return False


class UserProfilePermission(BasePermission):
    def has_permission(self, request, view):
        if (
            request.user.is_superuser or
            request.user.is_staff or
            request.user == view.get_object().user
        ):
            return True
