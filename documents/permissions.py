from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Custom permission to only allow access to owners of a document
    """

    def has_permission(self, request, view):
        if (view.queryset):
            return all([
                self.has_object_permission(request, view, doc)
                for doc in view.queryset
            ])
        return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsSelf(BasePermission):
    """
    Custom permission to only allow access user info to the user
    """

    def has_object_permission(self, request, view, obj):
        return obj.uid == request.user.uid
