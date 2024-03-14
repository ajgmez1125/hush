from rest_framework.serializers import ModelSerializer

from messaging.models import Conversation, Message, ConversationUser

class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class ConversationSerializer(ModelSerializer):
    class Meta:
        model = Conversation
        fields = '__all__'

class ConversationUserSerializer(ModelSerializer):
    class Meta:
        model = ConversationUser
        fields = '__all__'