from django.contrib import admin
from .models import Employee, EmployeeEmergencyContact


admin.site.register(Employee)
admin.site.register(EmployeeEmergencyContact)
