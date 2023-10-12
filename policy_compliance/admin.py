from django.contrib import admin
from .models import Compliance, TaxationPolicy


class TaxationPolicyAdmin(admin.ModelAdmin):
    list_display = ['country_code', 'tax_rate']


admin.site.register([Compliance, TaxationPolicy])
