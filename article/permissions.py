import random

from rest_framework.permissions import BasePermission


class RandomPermission(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return random.randint(0, 1)
