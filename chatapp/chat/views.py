from rest_framework import viewsets
from .models import ChatRoom, Message
from .serializers import ChatRoomSerializer, MessageSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class ChatRoomViewSet(viewsets.ModelViewSet):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    @action(detail=True, methods=["get"])
    def search(self, request, pk=None):
        query = request.query_params.get("q")
        if query:
            messages = Message.objects.filter(chat_room_id=pk, content__icontains=query)
            serializer = MessageSerializer(messages, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
