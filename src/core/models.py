from django.db import models
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from easy_thumbnails.fields import ThumbnailerField


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-
    updating ``created`` and ``modified`` fields
    """
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    modified = models.DateTimeField(_('Modified'), auto_now=True)

    class Meta:
        abstract = True


class AbstractPhoto(TimeStampedModel):
    image = ThumbnailerField(_('Image'), upload_to='related')
    ordering = models.PositiveIntegerField(
        _("Ordering"), default=0, blank=False, null=False)

    @property
    def target(self):
        raise NotImplementedError

    class Meta(object):
        abstract = True
        ordering = ['ordering', '-created']
        verbose_name = _('Photo')
        verbose_name_plural = _('Photos')
