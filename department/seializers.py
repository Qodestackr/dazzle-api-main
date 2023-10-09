from rest_framework import serializers
from .models import Department, Expense


class DepartmentSerializer(serializers.Serializer):
    class Meta:
        model = Department
        fields = '__all__'


class ExpenseSerializer(serializers.Serializer):
    class Meta:
        model = Expense
        fields = '__all__'
