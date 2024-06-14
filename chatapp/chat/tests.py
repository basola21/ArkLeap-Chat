from rest_framework.test import APITestCase
from rest_framework import status
from .models import ChatRoom, Message


class ChatRoomTests(APITestCase):
    def test_create_chat_room(self):
        response = self.client.post("/api/chatrooms/", {"name": "Test Room"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ChatRoom.objects.count(), 1)
        self.assertEqual(ChatRoom.objects.get().name, "Test Room")


class MessageTests(APITestCase):
    def test_create_message(self):
        chat_room = ChatRoom.objects.create(name="Test Room")
        response = self.client.post(
            f"/api/messages/", {"chat_room": chat_room.number, "content": "Hello"}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Message.objects.count(), 1)
        self.assertEqual(Message.objects.get().content, "Hello")
