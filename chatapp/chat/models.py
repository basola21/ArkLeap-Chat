from django.db import models


class ChatRoom(models.Model):
    number = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ChatRoom {self.number}"


class Message(models.Model):
    number = models.AutoField(primary_key=True)
    chat_room = models.ForeignKey(
        ChatRoom, related_name="messages", on_delete=models.CASCADE
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message {self.number} in ChatRoom {self.chat_room.number}"
