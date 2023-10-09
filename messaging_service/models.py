from django.db import models
from auth_service.models import CustomUser
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

    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text_tile = models.CharField(max_length=255)
    message = models.TextField()

    message_status = models.CharField(
        max_length=250, choices=message_status_options)

    messaging_channel = models.TextField(
        choices=messaging_channel_options)  # Recipient

    def delete_message(self):
        return ""


class NoticeBoard(TimeStampedModel):
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
    departments = models.ForeignKey(Department, on_delete=models.CASCADE)
