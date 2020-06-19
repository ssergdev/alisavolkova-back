from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import MessageCreateView


app_name = "feedback"
urlpatterns = [
    path("", csrf_exempt(MessageCreateView.as_view()), name="message-create")
]
