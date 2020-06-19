from django.db import models
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields, TranslatedField
from ckeditor.fields import RichTextField
from easy_thumbnails.fields import ThumbnailerField
from core.models import TimeStampedModel


class Slide(TimeStampedModel, TranslatableModel):
    text = TranslatedField(any_language=True)
    image = ThumbnailerField(_('Image'), upload_to='blocks', blank=True)
    translations = TranslatedFields(
        text=RichTextField(_("Text"), blank=True),
    )
    active = models.BooleanField(_("Active"), default=True)
    ordering = models.PositiveIntegerField(
        _("Ordering"), default=0, blank=False, null=False)


    def save(self, *args, **kwargs):
        """
        To avoid the thumbnail creations on user request,
        we perform the serialization on each model save method
        """
        from rest_framework.renderers import JSONRenderer
        from .serializers import SlideSerializer

        super().save(*args, **kwargs)
        JSONRenderer().render(SlideSerializer(self).data)

    def __str__(self):
        return f"Slide {self.pk}"

    class Meta(object):
        ordering = ["ordering"]
        verbose_name = _('Slide')
        verbose_name_plural = _('Slides')
