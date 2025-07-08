# ecommerce_api/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Unregister the default User admin to re-register it with custom fields
# This might raise an error if User is not yet registered.
# It's safer to try-except this if you anticipate this file being loaded before User is registered.
try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass # User model not yet registered, safe to proceed

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # Add 'is_staff' and 'is_superuser' to the list of fields displayed on the user change form
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_staff', 'is_superuser')}),
    )
    # Also ensure these are visible in the user list view if desired
    list_display = UserAdmin.list_display + ('is_staff', 'is_superuser')