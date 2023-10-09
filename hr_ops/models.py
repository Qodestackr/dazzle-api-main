from django.db import models
from auth_service.models import CustomUser
from employee.models import Employee
from department.models import Department
from common.timestamps import TimeStampedModel


class Audit(TimeStampedModel):
    audit_action_types = (
        ('CREATE', 'Create'),
        ('READ', 'Read'),
        ('UPDATE', 'Update'),
        ('DELETE', 'Delete'),

        ('USER_REGISTER', 'User Register'),
        ('USER_LOGIN', 'User Login'),
        ('USER_LOGOUT', 'User Logout'),
        ('USER_RESET_PASSWORD', 'User Reset Password'),
        ('GENERAL_SYSTEM_LOG', 'General System Log'),
        ('ADMIN_CREATE', 'Admin Create')
    )

    audit_id = models.CharField(max_length=255)  # TODO use uuid
    log_type = models.CharField(max_length=255, choices=audit_action_types)

    ip_address = models.GenericIPAddressField()
    user_id = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE)  # Employee
    # action => access log
    # departmentId


'''
department might have its own custom way of backups other than others. 
allow for that customization
'''


class DatabaseBackup(TimeStampedModel):
    data_backup_location = (
        ('EU', 'EU'),
        ('SA', 'SA'),
        ('US', 'US'),
        ('Middle East', 'Middle East')
    )

    schedule_backup_time = (
        ('SIX_HOURS', 'Six Hours'),
        ('MIDNIGHT', 'Midnight'),
        ('WEEKLY', 'WEEKLY'),
        ('MONTHLY', 'MONTHLY')
    )

    backup_name = models.CharField(max_length=255)
    backup_description = models.CharField(max_length=255)
    backup_location = models.CharField(
        max_length=250, choices=data_backup_location)

    last_backup = models.DateTimeField(auto_now=True)


'''
UserBehavior (or EmployeeBehavior) Model:

This model can capture data related to user behavior within the system.
It might include fields like user ID, action type, timestamp, and other relevant data for analyzing user interactions.
UserClassification Model:

To categorize users based on roles and permissions.
Fields might include user ID, role, and permissions.
Sales and Payment Model:

To track sales and payment data.
Fields could include transaction ID, product details, payment amount, date, and customer information.
OrgAnalytics Model:

To collect security, access logs, security incidents, and audit trails.
Fields may include event type, timestamp, user ID, IP address, and a description of the event.
SystemAnalytics Model:

For monitoring the overall health and performance of the HR Ops application.
Fields might include system metrics, timestamps, and descriptions of events or incidents.
DataBackup Model:

To manage data backups.
Fields could include backup name, description, location, and last backup timestamp.
ETL Workflow Model:

To manage ETL (Extract, Transform, Load) processes for data cleansing, structuring, and formatting.
Fields could include workflow name, description, status, and timestamps for different ETL stages.
Report Model:

To store generated reports and analytics results.
Fields might include report name, description, timestamp, and a link to the generated report file.
RoleBasedAccess Model:

To define and manage role-based access control for users.
Fields could include role name, permissions, and a list of users assigned to each role.
HRData Model:

To store HR-related data, such as employee information, HR policies, and other HR-related records.
Fields could include employee details, policies, and other HR-specific data.
Remember to establish appropriate relationships between these models to capture the data effectively. 
You can use ForeignKey, OneToOneField, or ManyToManyField relationships based on the specific requirements 
of your HR analytics and reporting application. Additionally, consider using Django's built-in user 
authentication system to handle user accounts and access control.
'''
