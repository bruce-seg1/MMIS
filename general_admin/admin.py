from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import UserProfile, Department, AuditLog

# Define an inline admin descriptor for UserProfile
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'
    fields = ('department', 'role', 'contact_phone') # Add other UserProfile fields here
    autocomplete_fields = ['department']


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_role', 'get_department')
    list_select_related = ('profile', 'profile__department')

    def get_role(self, instance):
        if hasattr(instance, 'profile'):
            return instance.profile.get_role_display()
        return None
    get_role.short_description = 'Role'

    def get_department(self, instance):
        if hasattr(instance, 'profile') and instance.profile.department:
            return instance.profile.department.name
        return None
    get_department.short_description = 'Department'

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'role', 'contact_phone')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'department__name', 'role')
    list_filter = ('role', 'department')
    autocomplete_fields = ['user', 'department']
    # This direct registration of UserProfile is useful for viewing all profiles or if a User object somehow doesn't have one.
    # However, primary management is intended via the User model's inline.

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'user', 'action', 'short_description')
    list_filter = ('action', 'timestamp', 'user')
    search_fields = ('user__username', 'description')
    readonly_fields = ('timestamp', 'user', 'action', 'description') # Make all fields read-only
    date_hierarchy = 'timestamp'

    def short_description(self, obj):
        return obj.description[:75] + '...' if len(obj.description) > 75 else obj.description
    short_description.short_description = 'Description'

    def has_add_permission(self, request):
        return False # Prevent adding audit logs manually through admin

    def has_change_permission(self, request, obj=None):
        return False # Prevent changing audit logs manually

    def has_delete_permission(self, request, obj=None):
        return False # Prevent deleting audit logs (unless superuser specifically needs to)
