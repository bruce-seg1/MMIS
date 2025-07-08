from django.contrib import admin
from .models import RevenueSource, RevenueCollection

@admin.register(RevenueSource)
class RevenueSourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(RevenueCollection)
class RevenueCollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'source', 'amount', 'date_collected', 'collected_by', 'receipt_number')
    list_filter = ('source', 'date_collected', 'collected_by')
    search_fields = ('source__name', 'receipt_number', 'collected_by__first_name', 'collected_by__last_name')
    autocomplete_fields = ['source', 'collected_by'] # For better UX in admin if you have many sources/employees
    date_hierarchy = 'date_collected'

    fieldsets = (
        (None, {
            'fields': ('source', 'amount', 'date_collected', 'receipt_number')
        }),
        ('Attribution & Notes', {
            'fields': ('collected_by', 'notes')
        }),
    )
