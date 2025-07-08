from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'first_name', 'last_name', 'job_title', 'email', 'employment_date')
    search_fields = ('first_name', 'last_name', 'employee_id', 'email')
    list_filter = ('job_title', 'employment_date')
    # readonly_fields = ('employee_id',) # If employee_id should not be editable once created

    fieldsets = (
        (None, {
            'fields': ('employee_id', 'first_name', 'last_name', 'email')
        }),
        ('Personal Information', {
            'fields': ('date_of_birth', 'gender', 'contact_number')
        }),
        ('Employment Details', {
            'fields': ('user', 'job_title', 'employment_date') # 'department' will be added here later
        }),
    )
