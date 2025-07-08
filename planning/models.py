from django.db import models
# from django.contrib.auth.models import User # Or link to a specific applicant user model if needed

class PermitApplication(models.Model):
    APPLICATION_TYPE_CHOICES = [
        ('BUILDING', 'Building Permit'),
        ('LAND_USE', 'Land Use Change'),
        ('ZONING', 'Zoning Request'),
        ('OTHER', 'Other'),
    ]
    STATUS_CHOICES = [
        ('SUBMITTED', 'Submitted'),
        ('UNDER_REVIEW', 'Under Review'),
        ('INSPECTION_SCHEDULED', 'Inspection Scheduled'),
        ('AWAITING_PAYMENT', 'Awaiting Payment'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
        ('WITHDRAWN', 'Withdrawn'), # Applicant withdrew
    ]

    application_id = models.CharField(max_length=30, unique=True, help_text="Unique ID for the application, e.g., BA/2024/0001")
    applicant_name = models.CharField(max_length=200, help_text="Full name of the individual or company applying")
    # applicant_contact = models.CharField(max_length=100, blank=True, help_text="Phone or email of applicant")
    application_type = models.CharField(max_length=20, choices=APPLICATION_TYPE_CHOICES)
    application_date = models.DateField(auto_now_add=True) # Automatically set when object is first created
    last_updated_date = models.DateField(auto_now=True) # Automatically set on save
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='SUBMITTED')
    property_location_details = models.TextField(help_text="Detailed address or plot number and location of the property")
    # project_description = models.TextField(blank=True, help_text="Brief description of the proposed project")
    # assigned_officer = models.ForeignKey('hr_payroll.Employee', on_delete=models.SET_NULL, null=True, blank=True, related_name='planning_applications')

    def __str__(self):
        return f"{self.get_application_type_display()} - {self.applicant_name} ({self.application_id})"

    class Meta:
        ordering = ['-application_date', 'applicant_name']

# Future models could include:
# class ApplicationDocument(models.Model):
#     application = models.ForeignKey(PermitApplication, on_delete=models.CASCADE, related_name='documents')
#     document_type = models.CharField(max_length=100, help_text="e.g., Site Plan, Architectural Drawing, Title Deed")
#     file = models.FileField(upload_to='planning_documents/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)

# class Inspection(models.Model):
#     application = models.ForeignKey(PermitApplication, on_delete=models.CASCADE, related_name='inspections')
#     inspection_date = models.DateTimeField()
#     inspector = models.ForeignKey('hr_payroll.Employee', on_delete=models.SET_NULL, null=True)
#     notes = models.TextField()
#     outcome = models.CharField(max_length=100, blank=True)
