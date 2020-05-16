from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from .constants import FRIEND_REQUEST_STATUS

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseModelWithUser(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='%(class)s_created_by')
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='%(class)s_updated_by', blank=True, null=True)

    class Meta:
        abstract = True


class Story(BaseModelWithUser):
    title = models.CharField(max_length=255)
    content = models.TextField()
    like_count = models.PositiveIntegerField(default=0)
    is_reported = models.BooleanField()
    reported_by = ArrayField(models.IntegerField(), blank=True, null=True)

    def __str__(self):
        return self.created_at.strftime('%Y-%m-%d %H:%M') + " - " + self.created_by.username + " - " + self.title

    class Meta:
        ordering = ['created_at']


class Comment(BaseModelWithUser):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    content = models.TextField()
    is_reported = models.BooleanField()
    reported_by = ArrayField(models.IntegerField(), blank=True, null=True)

    def __str__(self):
        return self.created_at.strftime('%Y-%m-%d %H:%M') + " - " + self.created_by.username + " - " + self.story.title

    class Meta:
        ordering = ['created_at']


class Like(BaseModelWithUser):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)

    def __str__(self):
        return self.created_at.strftime('%Y-%m-%d %H:%M') + " - " + self.created_by.username + " - " + self.story.title

    class Meta:
        ordering = ['created_at']


class Message(BaseModel):
    sender = models.ForeignKey(
        User, related_name="message_sender", on_delete=models.CASCADE)
    recipient = models.ForeignKey(
        User, related_name="message_recipient", on_delete=models.CASCADE)
    content = models.TextField()

    class Meta:
        ordering = ['created_at']


class MessageStatus(BaseModel):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
    read_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['created_at']


class FriendRequest(BaseModel):
    requested_by = models.ForeignKey(
        User, related_name="requested_by", on_delete=models.CASCADE)
    requested_to = models.ForeignKey(
        User, related_name="requested_to", on_delete=models.CASCADE)
    status = models.CharField(choices=FRIEND_REQUEST_STATUS, max_length=8)

    def __str__(self):
        return self.created_at.strftime('%Y-%m-%d %H:%M') + " - " + self.requested_by.username + " - " + self.requested_to.username
    
    class Meta:
        ordering = ['created_at']
