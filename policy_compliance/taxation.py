from decimal import Decimal
from django.db import models
from .models import TaxationPolicy

from .countries import (
    EU_COUNTRIES,
    NON_EU_UK,
    NORTH_AMERICAN_COUNTRIES,
    AFRICAN_COUNTRIES,
    SOUTH_AMERICAN_COUNTRIES
)


def get_tax_rate(country_code):
    try:
        policy = TaxationPolicy.objects.get(country_code=country_code)
        return policy.tax_rate
    except TaxationPolicy.DoesNotExist:
        return None  # Cases where country code is not found


def set_tax_rate(country_code, tax_rate):
    try:
        policy = TaxationPolicy.objects.get(country_code=country_code)
        policy.tax_rate = tax_rate
        policy.save()
        return True
    except TaxationPolicy.DoesNotExist:
        return False  # Cases where country code is not found


def is_country_compliant(country_code):
    try:
        policy = TaxationPolicy.objects.get(country_code=country_code)
        return policy.policy_rules_compliant
    except TaxationPolicy.DoesNotExist:
        return None  # Cases where country code is not found
