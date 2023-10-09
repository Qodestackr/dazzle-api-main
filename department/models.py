from django.db import models
from auth_service.models import CustomUser


class TimestampedModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ["-updated_at"]

    @classmethod
    def set_ordering(cls, ordering):
        cls._meta.ordering = ordering


class Department(TimestampedModel):
    deparment_name = models.CharField(max_length=255, primary_key=True)
    deparment_description = models.TextField()
    # deparment_policy_details = models.ForeignKey(Policy, on_delete=models.CASCADE)

    manager = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # expenses = models.ForeignKey(Expense, on_delete=models.CASCADE)
    # compliances = models.ForeignKey(Compliance, on_delete=models.CASCADE)
    # projects = models.ForeignKey(Project, on_delete=models.CASCADE)


class Expense(TimestampedModel):
    expense_type_options = (
        ('TRAVEL', 'Travel'),
        ('MEAL', 'Meal'),
        ('OFFICE_SUPPLY', 'Office Supply'),
        ('OTHER', 'Other')
    )

    expense_id = models.CharField(max_length=255)
    expense_description = models.CharField(max_length=255)
    expense_type = models.CharField(max_length=255)

    amount = models.DecimalField()

    department = models.ForeignKey(Department, on_delete=models.CASCADE)
