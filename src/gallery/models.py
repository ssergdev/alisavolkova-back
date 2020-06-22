from django.db import models
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields, TranslatedField
from ckeditor.fields import RichTextField
from easy_thumbnails.fields import ThumbnailerField
from core.models import TimeStampedModel, AbstractPhoto


class Tag(TimeStampedModel, TranslatableModel):
    name = TranslatedField(any_language=True)
    description = TranslatedField(any_language=True)

    translations = TranslatedFields(
        name=models.CharField(_("Name"), max_length=255),
        description=models.TextField(_("Description"), blank=True)
    )
    slug = models.SlugField(_("Slug"), max_length=255, unique=True)
    ordering = models.PositiveIntegerField(
        _("Ordering"), default=0, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta(object):
        ordering = ['ordering']
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')


class Artwork(TimeStampedModel, TranslatableModel):
    name = TranslatedField(any_language=True)
    description = TranslatedField(any_language=True)
    text = TranslatedField(any_language=True)
    history = TranslatedField(any_language=True)

    translations = TranslatedFields(
        name=models.CharField(_("Name"), max_length=255),
        description=models.TextField(_("Description")),
        text=RichTextField(_("Text"), blank=True),
        history=RichTextField(_("History"), blank=True)
    )
    image = ThumbnailerField(_('Image'), upload_to='gallery')
    tags = models.ManyToManyField(Tag, verbose_name=_('Tags'), blank=True)
    slug = models.SlugField(_("Slug"), max_length=255, unique=True)
    promote = models.BooleanField(_("Promote"), default=False)
    active = models.BooleanField(_("Active"), default=True)
    ordering = models.PositiveIntegerField(
        _("Ordering"), default=0, blank=False, null=False)

    @property
    def related(self):
        return Artwork.objects.filter(tags__in=self.tags.all()).exclude(pk=self.pk)\
            .annotate(num_common_tags=models.Count('pk')).order_by('-num_common_tags')[:4]

    def save(self, *args, **kwargs):
        """
        To avoid the thumbnail creations on user request,
        we perform the serialization on each model save method
        """
        from rest_framework.renderers import JSONRenderer
        from .serializers import ArtworkDetailSerializer

        super().save(*args, **kwargs)
        JSONRenderer().render(ArtworkDetailSerializer(self).data)

    def __str__(self):
        return self.name

    class Meta(object):
        ordering = ['ordering']
        verbose_name = _('Artwork')
        verbose_name_plural = _('Artworks')


class Photo(AbstractPhoto):
    target = models.ForeignKey(
        Artwork, related_name="photos", on_delete=models.CASCADE)
