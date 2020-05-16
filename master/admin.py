from django.contrib import admin
from master.models import Story, Like, Comment, Message, MessageStatus, FriendRequest
# Register your models here.
admin.site.register(Story)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Message)
admin.site.register(MessageStatus)
admin.site.register(FriendRequest)