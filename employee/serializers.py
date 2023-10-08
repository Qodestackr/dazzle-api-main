from rest_framework import serializers
from .models import Employee, EmployeeEmergencyContact


class EmployeeSerializer(serializers.Serializer):
    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeEmergencyContactSerializer(serializers.Serializer):
    class Meta:
        model = EmployeeEmergencyContact
        fields = '__all__'
