from django.contrib import admin
from .models import Expense, Department

admin.site.register([Expense, Department])