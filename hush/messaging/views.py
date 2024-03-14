from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from messaging.models import Conversation, ConversationUser, Message
from datetime import datetime
from messaging.serializer import MessageSerializer, ConversationSerializer, ConversationUserSerializer
import socket
import json

@api_view(['GET'])
def helloworld(request):
    return Response('hello world')

# Create your views here.
@api_view(['POST'])
def startconversation(request):
    data = json.loads(request.body)

    conversation = Conversation(
        name = data['name'],
        confidential = data['confidential'],
        password = data['password']
    )

    conversation_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    for port in range(49152,65565):
        try:
            conversation_socket.bind(('127.0.0.1', port))
            break
        except (socket.timeout, ConnectionRefusedError):
            continue
    
    conversation.port = conversation_socket.getsockname()[1]
    conversation.save()

    ConversationUser.objects.create(
        conversation_id = conversation,
        user_id = None
    )

    return Response({'code': 'Success',
                     'details': ConversationSerializer(conversation).data,
                     'socket': conversation_socket.getsockname()})

@api_view(['POST'])
def joinconversation(request, pk):
    try:
        conversation = Conversation.objects.get(id=pk)
    except:
        return Response('Room does not exist')

    data = json.loads(request.body)
    if(data['password'] == conversation.password):
        conv = ConversationUser.objects.create(
            conversation_id = conversation,
            user_id = None
        )
        return Response([
            'Success',
            ConversationUserSerializer(conv).data
        ])
    return Response('Could not join room')

@api_view(['POST'])
def sendmessage(request):
    conversation = Conversation.objects.get(id=request.POST.get('conversation_id'))
    message = Message(
        user_id = None,
        conversation_id = conversation,
        content = request.POST.get('content')
    )

    if(conversation.confidential == False):
        message.save()
    
    return Response([
        'Success',
        MessageSerializer(message).data
    ])