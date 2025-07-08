from django.db import models
# from django.contrib.auth.models import User # If collected_by refers directly to User
from hr_payroll.models import Employee # Assuming 'collected_by' is an Employee

class RevenueSource(models.Model):
    name = models.CharField(max_length=200, unique=True, help_text="e.g., Property Rate, Business Permit, Market Toll")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class RevenueCollection(models.Model):
    source = models.ForeignKey(RevenueSource, on_delete=models.PROTECT, related_name="collections", help_text="The source of this revenue")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_collected = models.DateField()
    collected_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, help_text="Employee who collected the revenue")
    # Or if using Django's User directly and not necessarily an Employee:
    # collected_by_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, help_text="User who recorded the collection")
    receipt_number = models.CharField(max_length=50, blank=True, null=True, unique=True, help_text="Optional unique receipt number")
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Collection of {self.amount} from {self.source.name} on {self.date_collected}"

    class Meta:
        ordering = ['-date_collected', '-id']
