from django.contrib import admin
from .models import BirthRegistration, DeathRegistration

@admin.register(BirthRegistration)
class BirthRegistrationAdmin(admin.ModelAdmin):
    list_display = ('registration_id', 'child_first_name', 'child_last_name', 'date_of_birth', 'gender', 'mother_full_name', 'father_full_name', 'registration_date', 'certificate_number')
    search_fields = ('registration_id', 'child_first_name', 'child_last_name', 'mother_full_name', 'father_full_name', 'certificate_number')
    list_filter = ('gender', 'registration_date', 'date_of_birth')
    date_hierarchy = 'registration_date'
    # readonly_fields = ('registration_id', 'registration_date')

    fieldsets = (
        ("Registration Info", {
            'fields': ('registration_id', 'certificate_number', 'registration_date') # 'registered_by'
        }),
        ("Child's Details", {
            'fields': ('child_first_name', 'child_last_name', 'date_of_birth', 'place_of_birth', 'gender')
        }),
        ("Parents' Details", {
            'fields': ('mother_full_name', 'father_full_name') # 'mother_occupation', 'father_occupation'
        }),
        # ("Informant Details", {
        #     'fields': ('informant_full_name', 'informant_relationship_to_child')
        # }),
        ("Notes", {
            'fields': ('notes',)
        }),
    )

@admin.register(DeathRegistration)
class DeathRegistrationAdmin(admin.ModelAdmin):
    list_display = ('registration_id', 'deceased_first_name', 'deceased_last_name', 'date_of_death', 'gender', 'age_at_death_years', 'registration_date', 'certificate_number')
    search_fields = ('registration_id', 'deceased_first_name', 'deceased_last_name', 'certificate_number')
    list_filter = ('gender', 'registration_date', 'date_of_death')
    date_hierarchy = 'registration_date'
    # readonly_fields = ('registration_id', 'registration_date')

    fieldsets = (
        ("Registration Info", {
            'fields': ('registration_id', 'certificate_number', 'registration_date') # 'registered_by'
        }),
        ("Deceased's Details", {
            'fields': ('deceased_first_name', 'deceased_last_name', 'gender', 'date_of_birth', 'date_of_death', 'place_of_death', 'age_at_death_years', 'cause_of_death') # 'deceased_other_names'
        }),
        # ("Medical Certification", {
        #     'fields': ('medical_certifier_name',)
        # }),
        # ("Informant Details", {
        #     'fields': ('informant_full_name', 'informant_relationship_to_deceased')
        # }),
        ("Notes", {
            'fields': ('notes',)
        }),
    )
