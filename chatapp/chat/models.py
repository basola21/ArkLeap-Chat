from django.db import models

"""
Here in the models file I always like to use a manager since I can customize it the way I want,
however this is a little bit more broken down than what I would tipicaly use it is this way for the sake
of demonstraing my refactoring approch
"""


class ChatRoomQuerySet(models.QuerySet):
    def active(self):
        return self.filter(is_active=True)


class ChatRoomManager(models.Manager):
    def get_queryset(self):
        return ChatRoomQuerySet(self.model, using=self._db)

    def create_chat_room(self, name):
        return self.create(name=name)


class ChatRoom(models.Model):
    number = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    objects = ChatRoomManager()

    def __str__(self):
        return f"ChatRoom {self.number}"


class MessageQuerySet(models.QuerySet):
    def by_chat_room(self, chat_room):
        return self.filter(chat_room=chat_room)

    def search_content(self, query):
        return self.filter(content__icontains=query)


class MessageManager(models.Manager):
    def get_queryset(self):
        return MessageQuerySet(self.model, using=self._db)

    def create_message(self, chat_room, content):
        return self.create(chat_room=chat_room, content=content)

    def by_chat_room(self, chat_room):
        return self.get_queryset().by_chat_room(chat_room)


class Message(models.Model):
    number = models.AutoField(primary_key=True)
    chat_room = models.ForeignKey(
        ChatRoom, related_name="messages", on_delete=models.CASCADE
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    objects = MessageManager()

    def __str__(self):
        return f"Message {self.number} in ChatRoom {self.chat_room.number}"
