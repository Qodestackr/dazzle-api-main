from django.contrib import admin
from .models import Audit, DatabaseBackup


admin.site.register([Audit, DatabaseBackup])
