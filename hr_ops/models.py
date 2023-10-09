from django.db import models
from auth_service import CustomUser
from employee import Employee


class TimestampedModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ["-updated_at"]

    @classmethod
    def set_ordering(cls, ordering):
        cls._meta.ordering = ordering


class Audit(TimestampedModel):
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


class DatabaseBackup(TimestampedModel):
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
