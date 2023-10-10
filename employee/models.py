from django.db import models
from auth_service.models import CustomUser
from django.utils.translation import gettext_lazy as _
from common.timestamps import TimeStampedModel
from department.models import Department


employee_status_options = (
    ('ACTIVE', 'Active'),
    ('ON_HOLD', 'On Hold'),  # short term basis
    ('EXTERNAL', 'External'),  # Managed by a third party
    ('SUSPENDED', 'Suspended'),
    ('CONTRACT_PENDING', 'Contract Pending'),
    ('CONTRACT_OVER', 'Contract Over'),
    ('CONTRACT_TERMINATED', 'Contract Terminated')
)

gender_options = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('OTHER', 'Other'),
)

employee_role_options = (
    ('BASIC', 'Basic Role'),
    ('EMPLOYEE', 'Employee'),
    ('SUPERVISOR', 'Supervisor'),
    ('SALES', 'Sales'),
    ('MARKETING', 'Marketing'),
    ('ENGINEERING', 'Engineering'),
    ('MANAGER', 'Manager'),
    ('HR_MANAGER', 'HR Manager'),  # super_admin
    ('TECHNICAL_SUPPORT', 'Technical Support'),
    ('DESIGNER', 'Designer'),
    ('FINANCE', 'Finance'),
    ('OPERATIONS', 'Operations'),
    ('QUALITY_ASSURANCE', 'Quality Assurance'),
    ('LEGAL', 'Legal'),
    ('RESEARCH', 'Research'),
    ('CUSTOMER_SUPPORT', 'Customer Support'),
    # More
)


class Employee(TimeStampedModel):
    ip_address = models.GenericIPAddressField(verbose_name=_(u'IP address'),
                                              blank=True, null=True, default=None)

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, db_index=True)
    gender = models.CharField(max_length=5, choices=gender_options)
    phone_number = models.CharField(max_length=50)
    job_title = models.CharField(max_length=255)
    employment_status = models.CharField(
        max_length=100, choices=employee_status_options)

    department = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    '''    kra_pin = models.CharField(max_length=255)
    nssf_number = models.CharField(max_length=255)
    role = models.CharField(
        max_length=50, choices=employee_role_options, default='BASIC')'''
    is_admin = models.BooleanField(default=False)

    # EMPLOYEE EXPENSES && EMPLOYEE TOOLS/DEVICES/...

    TimeStampedModel.set_ordering('created_at')


class EmployeeEmergencyContact(TimeStampedModel):
    dependent_contact = models.CharField(max_length=50, primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    department_relation = models.ForeignKey(
        Department, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Emergency Conctact'

    def contract_start_date(self):
        return "USE TIMESTAMPS"

    def contract_details(self):
        return "CONTRACT DETAILS"


'''
1. Employee Management:

List Employees: View a list of all employees.
Create Employee: Add new employees to the system.
Edit Employee: Update employee details.
Delete Employee: Remove employees from the system.
2. Attendance Records:

View Attendance Records: Display a list of attendance records for each employee.
Check-In: Allow employees to check in when they start their workday.
Check-Out: Allow employees to check out when they finish their workday.
3. Timesheet Records:

View Timesheet Records: Show a list of timesheet records for each employee.
Add Timesheet Entry: Allow employees to record their work hours and project details.
Edit Timesheet Entry: Update or edit existing timesheet records.
Delete Timesheet Entry: Remove or delete timesheet records.
4. Leave Management:

View Leave Requests: Display a list of leave requests.
Create Leave Request: Allow employees to request time off.
Approve or Reject Leave Request: Enable managers or administrators to review and approve/reject leave requests.
5. Holiday Management:

View Holidays: Show a list of holidays.
Add Holiday: Allow administrators to add new holidays.
6. Reporting:

Generate Reports: Create reports summarizing attendance and timesheet data for specific periods.
Export Data: Provide the ability to export data in various formats (e.g., CSV, Excel).
7. User Authentication and Authorization:

Implement user authentication and authorization to ensure that only authorized users can access specific views and perform actions.
8. User Dashboard:

Provide a user dashboard where employees can view their attendance records, timesheets, and leave balances.
9. Notifications:

Send email or in-app notifications to employees and managers about attendance, timesheets, and leave requests.
10. Data Validation and Error Handling:
- Implement validation for data entry to ensure accuracy and handle errors gracefully.

11. RESTful APIs:
- Create RESTful APIs for mobile apps or external systems to interact with your app.

12. User Profile and Settings:
- Allow employees to manage their profiles and settings, such as notification preferences.
'''
