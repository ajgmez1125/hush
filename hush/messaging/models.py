from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Conversation(models.Model):
    name = models.CharField(max_length=50, null=False, default='')
    created = models.DateTimeField(auto_now_add=True)
    confidential = models.BooleanField(default=True)
    password = models.CharField(max_length=50, null=False, default='')
    port = models.IntegerField(max_length = 65565, null = False)
    def __str__(self):
        return f"Conversation {self.id} created at {self.created} with password {self.password}"
    
class Message(models.Model):
    user_id = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    conversation_id = models.ForeignKey(Conversation, on_delete=models.SET_NULL, null=True)
    content = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.content
    
class ConversationUser(models.Model):
    conversation_id = models.ForeignKey(Conversation, on_delete=models.SET_NULL, null=True)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)