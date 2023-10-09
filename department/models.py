from django.db import models
from auth_service.models import CustomUser
from common.timestamps import TimeStampedModel
from policy_compliance.models import Compliance


class Expense(TimeStampedModel):
    """An expense incurred by a department."""

    expense_type_options = (
        ('TRAVEL', 'Travel'),
        ('MEAL', 'Meal'),
        ('OFFICE_SUPPLY', 'Office Supply'),
        ('OTHER', 'Other')
    )

    expense_id = models.CharField(max_length=255)
    expense_description = models.CharField(max_length=255)
    expense_type = models.CharField(
        max_length=255, choices=expense_type_options)

    amount = models.DecimalField(
        max_digits=10, decimal_places=2)  # Fixed field definition

    # department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_expense_type_display()}: {self.expense_description}"


class Department(TimeStampedModel):
    """A department within the company."""

    department_name = models.CharField(max_length=255, primary_key=True)
    department_description = models.TextField()
    # department_policy_details = models.ForeignKey(
    #     'Policy', on_delete=models.CASCADE)

    manager = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    expenses = models.ManyToManyField(Expense)
    compliances = models.ManyToManyField(Compliance)
    # projects = models.ManyToManyField('Project')

    def __str__(self):
        return self.department_name
