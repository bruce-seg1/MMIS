from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('ADMIN', 'Administrator'), # System-wide admin
        ('DEPT_HEAD', 'Department Head'),
        ('HR_OFFICER', 'HR Officer'),
        ('ACCOUNTANT', 'Accountant'),
        ('PLAN_OFFICER', 'Planning Officer'),
        ('REGISTRY_CLERK', 'Registry Clerk'),
        ('STAFF', 'General Staff'), # Basic user
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, related_name='staff_profiles')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='STAFF')
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    # employee_id = models.CharField(max_length=20, blank=True, null=True, help_text="Link to Employee model if not using the HR app's Employee.user field directly")


    def __str__(self):
        return f"{self.user.username}'s Profile ({self.get_role_display()})"

# Signal to create or update UserProfile whenever a User instance is saved.
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    # Ensure profile exists or create it. This handles both new users and existing users
    # who might not have a profile yet (e.g., created before this signal).
    profile, profile_created = UserProfile.objects.get_or_create(user=instance)

    # If the user is a superuser, assign them the ADMIN role by default.
    # This check should happen after ensuring the profile exists.
    if instance.is_superuser and profile.role != 'ADMIN':
        profile.role = 'ADMIN'
        profile.save()
    elif profile_created and instance.is_superuser : # If profile was just created for an existing superuser
        profile.role = 'ADMIN'
        profile.save()
    elif profile_created: # For newly created non-superuser, ensure default role is saved if not already set by get_or_create
        # This case might be redundant if UserProfile.role has a default and get_or_create respects it
        # but explicit save ensures the role is set.
        if not profile.role: # or check against the default explicitly
            profile.role = UserProfile._meta.get_field('role').default # Or 'STAFF'
            profile.save()


class AuditLog(models.Model):
    ACTION_CHOICES = [
        ('CREATE', 'Create'),
        ('UPDATE', 'Update'),
        ('DELETE', 'Delete'),
        ('LOGIN', 'Login'),
        ('LOGOUT', 'Logout'),
        ('VIEW', 'View'), # For sensitive views
        ('OTHER', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, help_text="User who performed the action")
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField(help_text="Description of the action performed")
    # content_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True, blank=True, help_text="Model affected")
    # object_id = models.PositiveIntegerField(null=True, blank=True, help_text="Primary key of the affected object")
    # affected_object = GenericForeignKey('content_type', 'object_id') # If you want to link to the specific object

    def __str__(self):
        user_str = self.user.username if self.user else "System"
        return f"{self.timestamp} - {user_str} - {self.action}: {self.description[:50]}"

    class Meta:
        ordering = ['-timestamp']
        verbose_name = "Audit Log"
        verbose_name_plural = "Audit Logs"
