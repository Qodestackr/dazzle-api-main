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
