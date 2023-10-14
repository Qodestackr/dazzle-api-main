from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions, viewsets, authentication
from .models import AttendanceRecord, TimesheetRecord
from .serializers import AttendanceRecordSerializer, TimesheetRecordSerializer


class AttendanceRecordList(generics.ListCreateAPIView):
    queryset = AttendanceRecord.objects.all()
    serializer_class = AttendanceRecordSerializer

    # pagination_class =
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class AttendanceRecordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AttendanceRecord.objects.all()
    serializer_class = AttendanceRecordSerializer

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class TimesheetRecordList(generics.ListCreateAPIView):
    queryset = TimesheetRecord.objects.all()
    serializer_class = TimesheetRecordSerializer

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class TimesheetRecordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TimesheetRecord.objects.all()
    serializer_class = TimesheetRecordSerializer

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


'''
Attendance Records:

View Attendance Records: Display a list of attendance records for each employee.
Check-In: Allow employees to check in when they start their workday.
Check-Out: Allow employees to check out when they finish their workday.

Timesheet Records:

View Timesheet Records: Show a list of timesheet records for each employee.
Add Timesheet Entry: Allow employees to record their work hours and project details.
Edit Timesheet Entry: Update or edit existing timesheet records.
Delete Timesheet Entry: Remove or delete timesheet records.
'''
