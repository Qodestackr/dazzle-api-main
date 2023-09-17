from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    '''
    To Scale The Auth and User Management, We need a Custom User Model with email as the
    unique ID for auth.
    '''

    def create_user(self, email, password, company_name, company_address, industry, employee_count, contact_person_name, contact_email, phone_number, subdomain, **extra_fields):
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            company_name=company_name,
            company_address=company_address,
            industry=industry,
            employee_count=employee_count,
            contact_person_name=contact_person_name,
            contact_email=contact_email,
            phone_number=phone_number,
            subdomain=subdomain,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)
