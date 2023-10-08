from django.db import models
from auth_service.models import CustomUser
from department.models import Department
import uuid


class TimestampedModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ["-updated_at"]

    @classmethod
    def set_ordering(cls, ordering):
        cls._meta.ordering = ordering


class Message(TimestampedModel):
    messaging_channel_options = (
        ('discord', 'Discord'),
        ('ms_teams', 'Microsoft Teams'),
        ('slack', 'Slack'),
        ('email', 'Email'),
        ('notification_push', 'Push Notification'),
        ('sms', 'SMS')
    )

    message_id = models.UUIDField(
        primary_key=True, default=uuid.uuid1(), db_index=True)
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text_tile = models.CharField(max_length=255)
    message = models.TextField()
    messaging_channel = models.TextField(choices=messaging_channel_options)

    def delete_message(self):
        return ""


class NoticeBoard(TimestampedModel):
    noticeboard_delete_after_options = (
        ('one_week', 'One Week'),
        ('one_month', 'One Month'),
        ('three_months', 'Three Months'),
        ('never', 'Never'),
    )

    noticeboard_id = models.UUIDField(
        primary_key=True, default=uuid.uuid1(), db_index=True)
    notice_title = models.CharField(max_length=255)
    # e.g alert of a new employee arrival etc
    notice_description = models.TextField()
    auto_delete_after = models.CharField(
        max_length=50, choices=noticeboard_delete_after_options)

    # departments = []  # all ids of deps
    departments = models.ForeignKey(Department, on_delete=models.CASCADE)
