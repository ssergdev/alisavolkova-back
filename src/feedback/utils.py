from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
import logging
logger = logging.getLogger(__name__)


def send_notification(message):
    context = {'instance': message}
    email_body = render_to_string('feedback/notification.txt', context)

    send_mail(
        message.subject,
        email_body,
        settings.SITE_EMAIL,
        [settings.SITE_EMAIL],
        fail_silently=False
    )
