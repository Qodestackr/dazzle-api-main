from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    '''
    CustomUserManager
    Attributes:
        - create_user
        - create_superuser
        - create_staffuser
    To Scale The Auth and User Management, We need a Custom User Model with email as the
    unique ID for auth.
    '''

    def create_user(self, email, password, company_name, company_address, industry, employee_count, contact_person_name, contact_email, phone_number, subdomain, **extra_fields):
        if not email:
            raise ValueError(_("User must have an Email"))

        if not password:
            raise ValueError(_("User must have a password"))

        if not company_name:
            raise ValueError(_("Company name must be set"))

        if not phone_number:
            raise ValueError(_("Phone number must be set"))

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
        user.set_password(password)  # TODO: use hash
        user.save()  # Vs user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):

        if not email:
            raise ValueError(_("User must have an Email"))

        if not password:
            raise ValueError(_("User must have a password"))

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)

    def create_staffuser(self, email, company_name, password=None):
        if not email:
            raise ValueError(_("Email must be set"))

        if not company_name:
            raise ValueError(_("Company name must be set"))

        if not password:
            raise ValueError(_("Password must be set"))

        email = self.normalize_email(email)

        user = self.model(
            email=email,
            company_name=company_name,
            password=password
        )

        return user
