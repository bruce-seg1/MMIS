from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, help_text="Link to Django User account for login if applicable")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=20, unique=True, help_text="Unique employee identifier")
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    contact_number = models.CharField(max_length=20, blank=True)
    email = models.EmailField(unique=True) # Should be unique for communication and if not using Django User email
    employment_date = models.DateField()
    job_title = models.CharField(max_length=100)
    # department = models.CharField(max_length=100) # We might make this a ForeignKey to a Department model later

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.employee_id})"

    class Meta:
        ordering = ['last_name', 'first_name']
