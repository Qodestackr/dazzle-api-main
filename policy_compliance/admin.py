from django.contrib import admin
from .models import Compliance, TaxationPolicy


admin.site.register(Compliance)
admin.site.register(TaxationPolicy)
