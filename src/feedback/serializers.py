from rest_framework import serializers
from .utils import send_notification
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"

    def create(self, validated_data):
        message = Message.objects.create(**validated_data)
        send_notification(message)
        return message
