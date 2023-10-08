from rest_framework import serializers
from .models import Department


class DepartmentSerializer(serializers.Serializer):
    class Meta:
        model = Department
        fields = '__all__'
