from rest_framework import serializers

from .models import Message, NoticeBoard


class MessageSerializer(serializers.Serializer):
    class Meta:
        model = Message
        fields = '__all__'


class NoticeBoardSerializer(serializers.Serializer):
    class Meta:
        model = NoticeBoard
        fields = '__all__'
