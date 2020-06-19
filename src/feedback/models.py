from django.db import models
from django.utils.translation import ugettext_lazy as _
from core.models import TimeStampedModel


class Message(TimeStampedModel):
    subject = models.CharField(_("Subject"), max_length=255)
    email = models.CharField(_("E-Mail"), max_length=255)
    name = models.CharField(_("Name"), max_length=255)
    text = models.TextField(_("Text"), blank=True)

    def __str__(self):
        return f"{self.subject} ({self.email})"

    class Meta(object):
        ordering = ["-created"]
        verbose_name = _('Message')
        verbose_name_plural = _('Messages')
