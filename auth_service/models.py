from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

role_options = (
    ('BASIC', 'Basic Role'),
    ('EMPLOYEE', 'Employee'),
    ('SUPERVISOR', 'Supervisor'),
    ('SALES', 'Sales'),
    ('MARKETING', 'Marketing'),
    ('ENGINEERING', 'Engineering'),
    ('MANAGER', 'Manager'),
    ('HR_MANAGER', 'HR Manager')  # super_admin
)


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

    role = models.CharField(
        max_length=255, choices=role_options, default='BASIC')

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    username = None

    # Specify the custom manager for this model
    objects = CustomUserManager()

    USERNAME_FIELD = "email"  # unique auth field

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
        return self.company_name


class UserProfile(models.Model):
    bio = models.TextField()
    img_url = models.URLField()
