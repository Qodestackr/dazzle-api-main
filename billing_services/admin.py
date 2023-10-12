from django.contrib import admin
from .models import Billing, Subscription, Invoice


admin.site.register([Billing, Subscription, Invoice])
