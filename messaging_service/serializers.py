from rest_framework import serializers

from .models import Message, NoticeBoard, Email, EmailConfiguration


class MessageSerializer(serializers.Serializer):
    class Meta:
        model = Message
        fields = '__all__'


class NoticeBoardSerializer(serializers.Serializer):
    class Meta:
        model = NoticeBoard
        fields = '__all__'


class EmailSerializer(serializers.Serializer):
    class Meta:
        model = Email
        fields = '__all__'


class EmailConfigurationSerializer(serializers.Serializer):
    class Meta:
        model = EmailConfiguration
        fields = '__all__'
