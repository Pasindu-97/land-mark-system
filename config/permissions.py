from rest_framework.permissions import BasePermission

from apps.users.models import User


class OfficePermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.is_authenticated:
            if user.type == User.Types.ADMIN:
                return True
            elif user.type == User.Types.OFFICE_STAFF:
                return True
            elif user.type == User.Types.COLLECTOR:
                return False
            elif user.type == User.Types.INVESTOR:
                return False
        return False


class CollectorPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.is_authenticated:
            if user.type == User.Types.ADMIN:
                return True
            elif user.type == User.Types.OFFICE_STAFF:
                return True
            elif user.type == User.Types.COLLECTOR:
                return True
            elif user.type == User.Types.INVESTOR:
                return False
        return False
