from django.contrib import admin
from .models import (Payroll, Tax, Deduction,
                     PayrollReport, PayrollTransaction)

models_to_register = [Payroll, Tax, Deduction,
                      PayrollReport, PayrollTransaction]

# for model in models_to_register:
#     admin.site.register(model)

admin.site.register(models_to_register)