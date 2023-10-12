from django.db import models
from auth_service.models import CustomUser
from django.conf import settings
from department.models import Department
from common.timestamps import TimeStampedModel
import uuid


class Message(TimeStampedModel):
    messaging_channel_options = (
        ('discord', 'Discord'),
        ('ms_teams', 'Microsoft Teams'),
        ('slack', 'Slack'),
        ('telegram', 'Telegram'),
        ('email', 'Email'),
        ('notification_push', 'Push Notification'),
        ('sms', 'SMS'),
        ('in_app', 'In-App Messaging'),
        ('all', 'All Channels')
    )

    message_status_options = (
        ('sending', 'Sending'),
        ('delivered', 'Delivered'),
        ('read', 'Read'),
        ('failed', 'Failed'),
    )

    message_id = models.UUIDField(
        primary_key=True, default=uuid.uuid1(), db_index=True)

    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text_tile = models.CharField(max_length=255)
    message = models.TextField()

    message_status = models.CharField(
        max_length=250, choices=message_status_options)

    messaging_channel = models.TextField(
        choices=messaging_channel_options)  # Recipient


class NoticeBoard(TimeStampedModel):
    '''
    NoticeBoard model
    This model allows admins to send a notice across moultiple departments, kinda notice boards on physical offices

    Attributes:
        - noticeboard_id
        - notice_title
        - notice_description
        - auto_delete_after: Will wipe out the notice after a select period of time, 
        - add_to_backup: Bool
        - departments: A list of departments to send to, all, select customs and so on.
    '''

    noticeboard_delete_after_options = (
        ('one_week', 'One Week'),
        ('one_month', 'One Month'),
        ('three_months', 'Three Months'),
        ('never', 'Never'),
    )

    noticeboard_id = models.UUIDField(
        primary_key=True, default=uuid.uuid1(), db_index=True)
    notice_title = models.CharField(max_length=255)
    notice_description = models.TextField()
    auto_delete_after = models.CharField(
        max_length=50, choices=noticeboard_delete_after_options)

    add_to_backup = models.BooleanField(default=False)

    # departments = models.ForeignKey(Department, on_delete=models.CASCADE)


class Email(models.Model):
    '''

    '''
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='email_created_by')
    subject = models.CharField(max_length=200)
    description = models.TextField()
    body = models.TextField()
    color = models.CharField(max_length=30)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject


class EmailConfiguration(models.Model):
    '''

    '''
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    email = models.TextField()
    host = models.TextField()
    port = models.IntegerField()
    use_tls = models.BooleanField(default=True)
    password = models.TextField()
    color = models.CharField(max_length=30)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.email} - {self.title}"
