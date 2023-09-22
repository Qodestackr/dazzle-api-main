from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    # Include custom fields in list_display
    list_display = ("email", "is_staff", "is_active", "company_name",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("HR Information", {
            "fields": (
                "company_name", "company_address", "industry",
                "employee_count", "contact_person_name", "contact_email",
                "phone_number", "subdomain"
            ),
        }),
        ("Permissions", {"fields": ("is_staff",
         "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions",
                "company_name", "company_address", "industry",
                "employee_count", "contact_person_name", "contact_email",
                "phone_number", "subdomain"
            ),
        }),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)
