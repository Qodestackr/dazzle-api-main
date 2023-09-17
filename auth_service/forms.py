from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email", "company_name", "company_address", "industry", "employee_count",
                  "contact_person_name", "contact_email", "phone_number", "subdomain",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email", "company_name", "company_address", "industry", "employee_count",
                  "contact_person_name", "contact_email", "phone_number", "subdomain",)
