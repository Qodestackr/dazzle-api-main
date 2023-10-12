from rest_framework import serializers
from .models import Compliance, TaxationPolicy


class ComplianceSerializer(serializers.Serializer):
    class Meta:
        model = Compliance
        fields = ['compliance_id', 'compliance_type', 'compliance_description']


class TaxationPolicySerializer(serializers.Serializer):
    class Meta:
        model = TaxationPolicy
        fields = ['country_code', 'tax_rate']
