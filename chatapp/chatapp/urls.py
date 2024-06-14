from django.urls import path, include
from rest_framework.routers import DefaultRouter
from chat.views import ChatRoomViewSet, MessageViewSet
from django.contrib import admin

router = DefaultRouter()
router.register(r"chatrooms", ChatRoomViewSet)
router.register(r"messages", MessageViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
