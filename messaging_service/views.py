from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication

from .models import Message, Email, EmailConfiguration, NoticeBoard
from .serializers import (
    MessageSerializer,
    EmailSerializer,
    EmailConfigurationSerializer,
    NoticeBoardSerializer)


# def delete_message_view(request, message_id):
#     '''
#     Retrieves and deletes message based on message_id
#     '''
#     message = get_object_or_404(Message, message_id=message_id)

#     message.delete_message()

#     return {
#         'message': 'Delete Successful',
#         'status': 200
#     }


# def sendepasswordresetmail(user, token):
# def sendaccountactivationemail(user):

class MessageViewSet(viewsets.ViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    authentication_classes = [TokenAuthentication]
    # throttle_classes = api_settings.DEFAULT_THROTTLE_CLASSES
    permission_classes = [permissions.IsAuthenticated]


class EmailViewSet(viewsets.ViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class EmailConfigurationViewSet(viewsets.ViewSet):
    queryset = EmailConfiguration.objects.all()
    serializer_class = EmailConfigurationSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class NoticeBoardViewSet(viewsets.ViewSet):
    queryset = NoticeBoard.objects.all()
    serializer_class = NoticeBoardSerializer
    authentication_classes = [TokenAuthentication]
    permission_clases = [permissions.IsAuthenticated]
