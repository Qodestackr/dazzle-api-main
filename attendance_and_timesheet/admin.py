from django.contrib import admin
from .models import TimesheetRecord, AttendanceRecord, Holiday

admin.site.register([TimesheetRecord, AttendanceRecord, Holiday])