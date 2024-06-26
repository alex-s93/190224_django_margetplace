from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request


class IsCustomerOrReadOnly(BasePermission):

    def has_object_permission(self, request: Request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user == obj.customer