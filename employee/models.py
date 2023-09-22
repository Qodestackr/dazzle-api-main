from django.db import models
from auth_service.models import CustomUser

employee_status_options = (
    ('ACTIVE', 'Active'),
    ('ON_HOLD', 'On Hold'),  # short term basis
    ('EXTERNAL', 'External'),  # Managed by a third party
    ('SUSPENDED', 'Suspended'),
    ('CONTRACT_PENDING', 'Contract Pending'),
    ('CONTRACT_OVER', 'Contract Over'),
    ('CONTRACT_TERMINATED', 'Contract Terminated')
)

gender_options = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)


class TimestampedModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ["-updated_at"]

    @classmethod
    def set_ordering(cls, ordering):
        cls._meta.ordering = ordering


class Employee(TimestampedModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, db_index=True)
    gender = models.CharField(max_length=5, choices=gender_options)
    phone_number = models.CharField(max_length=50)
    job_title = models.CharField(max_length=255)
    employment_status = models.CharField(
        max_length=100, choices=employee_status_options)

    department = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    is_admin = models.BooleanField(default=False)

    TimestampedModel.set_ordering('created_at')


class EmployeeEmergencyContact(TimestampedModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    department_relation = models.CharField(max_length=100)
    dependent_contact = models.CharField(max_length=50)

    def contract_start_date(self):
        return "USE TIMESTAMPS"

    def contract_details(self):
        return "CONTRACT DETAILS"
