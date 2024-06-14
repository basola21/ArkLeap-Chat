from rest_framework.test import APITestCase
from rest_framework import status
from .models import ChatRoom, Message


class ChatRoomTests(APITestCase):
    def test_create_chat_room(self):
        response = self.client.post("/api/chatrooms/", {"name": "Test Room"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ChatRoom.objects.count(), 1)
        self.assertEqual(ChatRoom.objects.get().name, "Test Room")

    def test_read_chat_room(self):
        chat_room = ChatRoom.objects.create(name="Test Room")
        response = self.client.get(f"/api/chatrooms/{chat_room.number}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Test Room")

    def test_update_chat_room(self):
        chat_room = ChatRoom.objects.create(name="Test Room")
        response = self.client.put(
            f"/api/chatrooms/{chat_room.number}/", {"name": "Updated Room"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ChatRoom.objects.get().name, "Updated Room")

    def test_list_chat_rooms(self):
        ChatRoom.objects.create(name="Test Room 1")
        ChatRoom.objects.create(name="Test Room 2")
        response = self.client.get("/api/chatrooms/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


class MessageTests(APITestCase):
    def test_create_message(self):
        chat_room = ChatRoom.objects.create(name="Test Room")
        response = self.client.post(
            "/api/messages/", {"chat_room": chat_room.number, "content": "Hello"}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Message.objects.count(), 1)
        self.assertEqual(Message.objects.get().content, "Hello")

    def test_read_message(self):
        chat_room = ChatRoom.objects.create(name="Test Room")
        message = Message.objects.create(chat_room=chat_room, content="Hello")
        response = self.client.get(f"/api/messages/{message.number}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["content"], "Hello")

    def test_update_message(self):
        chat_room = ChatRoom.objects.create(name="Test Room")
        message = Message.objects.create(chat_room=chat_room, content="Hello")
        response = self.client.put(
            f"/api/messages/{message.number}/",
            {"chat_room": chat_room.number, "content": "Updated Hello"},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Message.objects.get().content, "Updated Hello")

    def test_list_messages(self):
        chat_room = ChatRoom.objects.create(name="Test Room")
        Message.objects.create(chat_room=chat_room, content="Hello 1")
        Message.objects.create(chat_room=chat_room, content="Hello 2")
        response = self.client.get("/api/messages/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_search_messages(self):
        chat_room = ChatRoom.objects.create(name="Test Room")
        Message.objects.create(chat_room=chat_room, content="Hello world")
        Message.objects.create(chat_room=chat_room, content="Another message")
        response = self.client.get(f"/api/messages/{chat_room.number}/search/?q=Hello")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["content"], "Hello world")
