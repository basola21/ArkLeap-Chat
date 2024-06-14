from rest_framework import viewsets, status
from .models import ChatRoom, Message
from .serializers import ChatRoomSerializer, MessageSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

"""
Here in the views I like to use simple build in functions whenever posible so as you can see it is not too long and easy to understand.
"""


class ChatRoomViewSet(viewsets.ModelViewSet):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer

    def get_queryset(self):
        return ChatRoom.objects.all()


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.objects.all()

    @action(detail=True, methods=["get"])
    def search(self, request, pk=None):
        query = request.query_params.get("q")
        if query:
            chat_room = get_object_or_404(ChatRoom, pk=pk)
            messages = Message.objects.by_chat_room(chat_room).search_content(query)
            serializer = MessageSerializer(messages, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
