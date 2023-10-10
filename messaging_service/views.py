from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Message


def delete_message_view(request, message_id):
    '''
    Retrieves and deletes message based on message_id
    '''
    message = get_object_or_404(Message, message_id=message_id)

    message.delete_message()

    return {
        'message': 'Delete Successful',
        'status': 200
    }
