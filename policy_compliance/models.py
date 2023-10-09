from django.db import models
# from department.models import Department
from common.timestamps import TimeStampedModel


class TaxationPolicy(TimeStampedModel):
    country_code = models.CharField(max_length=2, unique=True)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name_plural = "Taxation Policies"

    def __str__(self):
        return f"{self.country_code} - Tax Rate: {self.tax_rate}%"


class Compliance(TimeStampedModel):
    compliance_type_options = (
        ('HEALTH', 'Health'),
        ('SYSTEM_SECURITY', 'System Security'),
        ('HIPAA', 'HIPAA'),  # Health
        ('GDPR', 'GDPR'),  # General Data Protection Regulation
        ('OSHA', 'OSHA'),  # Occupation Safety and Health Admin
        ('FLSA', 'FLSA'),  # Fair Labor Standard Act
        ('PWDS', 'PWDS'),  # ...with dissabilities got some tax exceptions
    )

    compliance_id = models.CharField(max_length=255)
    compliance_description = models.CharField(max_length=255)

    compliance_type = models.CharField(max_length=255, )

    # department = models.ForeignKey(Department, on_delete=models.CASCADE)
