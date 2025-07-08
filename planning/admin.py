from django.contrib import admin
from .models import PermitApplication #, ApplicationDocument, Inspection (if/when added)

@admin.register(PermitApplication)
class PermitApplicationAdmin(admin.ModelAdmin):
    list_display = ('application_id', 'applicant_name', 'application_type', 'status', 'application_date', 'last_updated_date')
    list_filter = ('application_type', 'status', 'application_date')
    search_fields = ('application_id', 'applicant_name', 'property_location_details')
    date_hierarchy = 'application_date'
    # readonly_fields = ('application_id', 'application_date', 'last_updated_date') # If ID is auto-generated or set elsewhere

    fieldsets = (
        (None, {
            'fields': ('application_id', 'applicant_name', 'application_type', 'status')
        }),
        ('Details', {
            'fields': ('property_location_details', ) # 'project_description'
        }),
        ('Timeline', {
            'fields': ('application_date', 'last_updated_date')
        }),
        # ('Assignment', {
        #     'fields': ('assigned_officer',)
        # })
    )

    # If you add inlines for documents or inspections later:
    # inlines = [ApplicationDocumentInline, InspectionInline] # Define these inline classes

# Example for when ApplicationDocument model is created:
# class ApplicationDocumentInline(admin.TabularInline):
# model = ApplicationDocument
#     extra = 1 # Number of empty forms to display
#     fields = ('document_type', 'file')

# Example for when Inspection model is created:
# class InspectionInline(admin.TabularInline):
# model = Inspection
#     extra = 0
#     fields = ('inspection_date', 'inspector', 'outcome', 'notes')
#     autocomplete_fields = ['inspector']
