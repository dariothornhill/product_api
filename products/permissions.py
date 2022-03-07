from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user.is_admin

from rest_framework import permissions


class IsOwnerOrCreate(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'POST':
            return True
        if request.method == 'GET':
            return obj.owner == request.user
        return False