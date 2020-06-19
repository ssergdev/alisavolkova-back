from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    fields = ["email", "name", "subject", "text"]
    list_display = ["subject", "email", "name", "created", "modified"]
    list_display_links = ["subject", "email", "name"]
    list_filter = ["created"]
    serach_fields = ["subject", "name", "email"]


admin.site.register(Message, MessageAdmin)
