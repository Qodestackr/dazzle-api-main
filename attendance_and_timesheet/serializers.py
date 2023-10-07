from rest_framework import serializers
from .models import AttendanceRecord, TimesheetRecord


class AttendanceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceRecord
        fields = '__all__'


class TimesheetRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimesheetRecord
        fields = '__all__'
