from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    email = models.EmailField(_("Email Field"), unique=True)
    company_name = models.CharField(max_length=255)
    company_address = models.TextField()
    industry = models.CharField(max_length=255)
    employee_count = models.PositiveIntegerField()
    contact_person_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    subdomain = models.CharField(max_length=50, unique=True)

    # Username field is not needed since you're using email as the unique identifier.
    # Remove the following line:
    username = None

    # Specify the custom manager for this model
    objects = CustomUserManager()

    # You may want to add any additional fields you require.

    # Define the field that uniquely identifies a user (used for authentication).
    USERNAME_FIELD = "email"

    # Add any additional fields that are required when creating a user.
    REQUIRED_FIELDS = [
        'company_name',
        'company_address',
        'industry',
        'employee_count',
        'contact_person_name',
        'contact_email',
        'phone_number',
        'subdomain',
    ]

    def __str__(self) -> str:
        return self.email
