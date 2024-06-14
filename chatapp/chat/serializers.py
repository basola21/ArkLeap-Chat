from rest_framework import serializers
from .models import ChatRoom, Message


class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = ["number", "name", "created_at"]


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["number", "chat_room", "content", "created_at"]
