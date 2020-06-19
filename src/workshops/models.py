from django.db import models
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields, TranslatedField
from easy_thumbnails.fields import ThumbnailerField
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from core.models import TimeStampedModel, AbstractPhoto


class Workshop(TimeStampedModel, TranslatableModel):
    name = TranslatedField(any_language=True)
    description = TranslatedField(any_language=True)
    text = TranslatedField(any_language=True)
    place = TranslatedField(any_language=True)

    translations = TranslatedFields(
        name=models.CharField(_("Name"), max_length=255),
        description=RichTextField(_("Description")),
        text=RichTextUploadingField(_("Text")),
        place=models.CharField(_("Place"), max_length=255)
    )
    image = ThumbnailerField(_('Image'), upload_to="workshops")
    date_start = models.DateField(_("Date start"))
    date_end = models.DateField(_("Date end"), null=True, blank=True)
    active = models.BooleanField(_("Active"), default=True)
    slug = models.SlugField(_("Slug"), max_length=255, unique=True)
    ordering = models.PositiveIntegerField(
        _("Ordering"), default=0, blank=False, null=False)

    def save(self, *args, **kwargs):
        """
        To avoid the thumbnail creations on user request,
        we perform the serialization on each model save method
        """
        from rest_framework.renderers import JSONRenderer
        from .serializers import WorkshopDetailSerializer

        super().save(*args, **kwargs)
        JSONRenderer().render(WorkshopDetailSerializer(self).data)

    def __str__(self):
        return self.name

    class Meta(object):
        ordering = ["-created"]
        verbose_name = _('Workshop')
        verbose_name_plural = _('Workshops')


class Photo(AbstractPhoto):
    target = models.ForeignKey(
        Workshop, related_name="photos", on_delete=models.CASCADE)
