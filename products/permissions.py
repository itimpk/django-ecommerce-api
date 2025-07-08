# products/permissions.py
from rest_framework import permissions

# Custom Permission for Admin Users
class IsAdminUser(permissions.BasePermission):
    """
    Allows access only to admin users (is_superuser).
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_superuser

# Custom Permission for Seller Users (and Admins)
class IsSellerUserOrAdmin(permissions.BasePermission):
    """
    Allows access only to authenticated users who are staff (is_staff) or superusers.
    This assumes 'staff' users are your 'sellers'.
    """
    def has_permission(self, request, view):
        # Read permissions are allowed to any request, so we'll only check permissions for write operations
        if request.method in permissions.SAFE_METHODS: # GET, HEAD, OPTIONS
            return True

        # Write permissions are only allowed to authenticated staff or superuser users.
        return request.user and request.user.is_authenticated and (request.user.is_staff or request.user.is_superuser)

# Permission for Customers (Read-Only)
class IsCustomerUser(permissions.BasePermission):
    """
    Allows read access to all authenticated users, but no write access.
    This can be used for 'customer' type users.
    """
    def has_permission(self, request, view):
        # Read-only permissions are allowed for any authenticated user.
        return request.user and request.user.is_authenticated and request.method in permissions.SAFE_METHODS