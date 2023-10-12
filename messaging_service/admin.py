from django.contrib import admin
from .models import Message, NoticeBoard, Email, EmailConfiguration

admin.site.register([Message, NoticeBoard, Email, EmailConfiguration])
