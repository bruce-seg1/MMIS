from django.db import models
# from hr_payroll.models import Employee # If a registrar employee is linked

class BirthRegistration(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    # Unique registration ID, could be auto-generated or manually entered
    registration_id = models.CharField(max_length=30, unique=True, help_text="e.g., BREG/2024/0001")

    child_first_name = models.CharField(max_length=100)
    child_last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=200, help_text="Hospital, Clinic, Home Address, etc.")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    father_full_name = models.CharField(max_length=200, blank=True, null=True)
    # father_occupation = models.CharField(max_length=100, blank=True, null=True)
    mother_full_name = models.CharField(max_length=200)
    # mother_occupation = models.CharField(max_length=100, blank=True, null=True)

    # informant_full_name = models.CharField(max_length=200, help_text="Person reporting the birth")
    # informant_relationship_to_child = models.CharField(max_length=100, blank=True)

    registration_date = models.DateField(auto_now_add=True)
    certificate_number = models.CharField(max_length=50, unique=True, blank=True, null=True, help_text="Official certificate number, if issued")
    # registered_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='births_registered')

    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Birth: {self.child_first_name} {self.child_last_name} ({self.registration_id})"

    class Meta:
        ordering = ['-registration_date', 'child_last_name', 'child_first_name']
        verbose_name = "Birth Registration"
        verbose_name_plural = "Birth Registrations"


class DeathRegistration(models.Model):
    # Unique registration ID
    registration_id = models.CharField(max_length=30, unique=True, help_text="e.g., DREG/2024/0001")

    deceased_first_name = models.CharField(max_length=100)
    deceased_last_name = models.CharField(max_length=100)
    # deceased_other_names = models.CharField(max_length=100, blank=True, null=True)

    gender = models.CharField(max_length=1, choices=BirthRegistration.GENDER_CHOICES) # Reusing choices
    date_of_birth = models.DateField(blank=True, null=True) # May not always be known precisely
    date_of_death = models.DateField()
    place_of_death = models.CharField(max_length=200, help_text="Hospital, Clinic, Home Address, etc.")
    age_at_death_years = models.PositiveIntegerField(blank=True, null=True, help_text="Calculated or provided age in years")
    # age_at_death_months = models.PositiveIntegerField(blank=True, null=True)
    # age_at_death_days = models.PositiveIntegerField(blank=True, null=True)

    cause_of_death = models.CharField(max_length=255, blank=True, help_text="Primary cause of death")
    # medical_certifier_name = models.CharField(max_length=200, blank=True, help_text="Name of doctor or medical officer")

    # informant_full_name = models.CharField(max_length=200, help_text="Person reporting the death")
    # informant_relationship_to_deceased = models.CharField(max_length=100, blank=True)

    registration_date = models.DateField(auto_now_add=True)
    certificate_number = models.CharField(max_length=50, unique=True, blank=True, null=True, help_text="Official certificate number, if issued")
    # registered_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='deaths_registered')

    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Death: {self.deceased_first_name} {self.deceased_last_name} ({self.registration_id})"

    class Meta:
        ordering = ['-registration_date', 'deceased_last_name', 'deceased_first_name']
        verbose_name = "Death Registration"
        verbose_name_plural = "Death Registrations"
