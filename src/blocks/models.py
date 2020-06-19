from django.db import models
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields, TranslatedField
from ckeditor_uploader.fields import RichTextUploadingField
from easy_thumbnails.fields import ThumbnailerField
from core.models import TimeStampedModel


class Block(TimeStampedModel, TranslatableModel):
    text = TranslatedField(any_language=True)

    type = models.CharField(
        _("Type"),
        choices=[
            ('text', _("Text")),
            ('image', _("Image"))
        ],
        max_length=16,
        default='text',
    )
    slug = models.SlugField(_("Slug"), max_length=255,
                            unique=True, blank=False)
    image = ThumbnailerField(upload_to='blocks', blank=True)
    translations = TranslatedFields(
        text=RichTextUploadingField(_("Text"), blank=True),
    )

    def save(self, *args, **kwargs):
        """
        To avoid the thumbnail creations on user request,
        we perform the serialization on each model save method
        """
        from rest_framework.renderers import JSONRenderer
        from .serializers import BlockSerializer

        super().save(*args, **kwargs)
        JSONRenderer().render(BlockSerializer(self).data)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = _('Fragment')
        verbose_name_plural = _('Fragments')
