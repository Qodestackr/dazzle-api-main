from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework import permissions, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Employee, EmployeeEmergencyContact
from .serializers import EmployeeSerializer, EmployeeEmergencyContactSerializer


class EmployeeViewSet(viewsets.ViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class EmployeeEmergencyContactViewSet(viewsets.ViewSet):
    queryset = EmployeeEmergencyContact.objects.all()
    serializer_class = EmployeeEmergencyContactSerializer

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


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

Leave Management:

View Leave Requests: Display a list of leave requests.
Create Leave Request: Allow employees to request time off.
Approve or Reject Leave Request: Enable managers or administrators to review and approve/reject leave requests.

Holiday Management:

View Holidays: Show a list of holidays.
Add Holiday: Allow administrators to add new holidays.

Reporting:

Generate Reports: Create reports summarizing attendance and timesheet data for specific periods.
Export Data: Provide the ability to export data in various formats (e.g., CSV, Excel).

User Dashboard:

Provide a user dashboard where employees can view their attendance records, timesheets, 
and leave balances.

10. Data Validation and Error Handling:
- Implement validation for data entry to ensure accuracy and handle errors gracefully.

11. RESTful APIs:
- Create RESTful APIs for mobile apps or external systems to interact with your app.

12. User Profile and Settings:
- Allow employees to manage their profiles and settings, such as notification preferences.
'''
