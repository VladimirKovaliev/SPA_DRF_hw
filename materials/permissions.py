from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsModerator(BasePermission):
    message = 'вы не модератор'

    def has_permission(self, request, view):
        if request.user.role == UserRoles.MODERATOR:
            return True
        return False


class IsOwner(BasePermission):
    message = 'вы не владелец'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False
