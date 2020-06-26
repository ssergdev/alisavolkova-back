from django.urls import path
from .views import MessageCreateView


app_name = "feedback"
urlpatterns = [
    path("", MessageCreateView.as_view(), name="message-create")
]
