from rest_framework import serializers
from .models import Payroll, PayrollReport, PayrollTransaction, Deduction, Tax


class PayrollSerializer(serializers.Serializer):
    class Meta:
        model = Payroll
        fields = '__all__'


class PayrollReportSerializer(serializers.Serializer):
    class Meta:
        model = PayrollReport
        fields = '__all__'


class PayrollTransactionSerializer(serializers.Serializer):
    class Meta:
        model = PayrollTransaction
        fields = '__all__'


class DeductionSerializer(serializers.Serializer):
    class Meta:
        model = Deduction
        fields = '__all__'


class TaxSerializer(serializers.Serializer):
    class Meta:
        model = Tax
        fields = '__all__'
