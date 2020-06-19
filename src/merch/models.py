from django.db import models
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields, TranslatedField
from easy_thumbnails.fields import ThumbnailerField
from ckeditor.fields import RichTextField
from djmoney.models.fields import MoneyField
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
        ordering = ["ordering"]
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')


class Product(TimeStampedModel, TranslatableModel):
    name = TranslatedField(any_language=True)
    description = TranslatedField(any_language=True)

    translations = TranslatedFields(
        name=models.CharField(_("Name"), max_length=255),
        description=RichTextField(_("Description"))
    )
    price = MoneyField(
        verbose_name=_('Price'),
        max_digits=14,
        decimal_places=2,
        null=True,
        blank=True,
        default_currency="USD",
    )
    image = ThumbnailerField(_('Image'), upload_to="gallery")
    tags = models.ManyToManyField(Tag, verbose_name=_('Tags'), blank=True)
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
        from .serializers import ProductDetailSerializer

        super().save(*args, **kwargs)
        JSONRenderer().render(ProductDetailSerializer(self).data)

    def __str__(self):
        return self.name

    class Meta(object):
        ordering = ["ordering"]
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class Photo(AbstractPhoto):
    target = models.ForeignKey(
        Product, related_name="photos", on_delete=models.CASCADE)
