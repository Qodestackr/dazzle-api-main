from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import AttendanceRecord, TimesheetRecord
from .serializers import AttendanceRecordSerializer, TimesheetRecordSerializer


class AttendanceRecordList(generics.ListCreateAPIView):
    queryset = AttendanceRecord.objects.all()
    serializer_class = AttendanceRecordSerializer


class AttendanceRecordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AttendanceRecord.objects.all()
    serializer_class = AttendanceRecordSerializer


class TimesheetRecordList(generics.ListCreateAPIView):
    queryset = TimesheetRecord.objects.all()
    serializer_class = TimesheetRecordSerializer


class TimesheetRecordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TimesheetRecord.objects.all()
    serializer_class = TimesheetRecordSerializer
