from rest_framework.permissions import BasePermission


class ObjectPermission(BasePermission):
    
    def has_permission(self, request, view):
        
        if view.action == 'list':
            return request.user.is_superuser
        elif view.action == 'create':
            return request.user.id == request.data.get('user')
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):

        if view.action in ['retrieve', 'update', 'partial_update'] and view.basename != 'user':
            return request.user.id == obj.user.id or request.user.is_superuser
        elif view.action == 'destroy':
            return request.user.is_superuser
        else:
            return request.user.id == obj.id or request.user.is_superuser

