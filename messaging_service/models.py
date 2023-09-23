from django.db import models
from auth_service.models import CustomUser
import uuid

noticeboard_delete_after_options = (
    ('one_week', 'One Week'),
    ('one_month', 'One Month'),
    ('three_months', 'Three Months'),
    ('never', 'Never'),
)


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
    message_id = models.UUIDField(
        primary_key=True, db_index=True)  # default=uuid.uuid5(namespace='', name=''),
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text_tile = models.CharField(max_length=255)
    message = models.TextField()

    def delete_message(self):
        return ""


# Slack, Discord, etc


class NoticeBoard(TimestampedModel):
    notice_title = models.CharField(max_length=255)
    # e.g alert of a new employee arrival etc
    notice_description = models.TextField()
    auto_delete_after = models.CharField(
        max_length=50, choices=noticeboard_delete_after_options)

    # departments = []  # all ids of deps
