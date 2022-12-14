




# -*- coding: utf-8 -*-
from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    message = "Not an owner."

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner

    # def has_permission(self, request, view):
    #     return True
