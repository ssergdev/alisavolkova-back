from rest_framework.generics import CreateAPIView
from .serializers import MessageSerializer
from .models import Message


class MessageCreateView(CreateAPIView):
    permission_classes = ()
    authentication_classes = ()
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    authentication_classes = []
