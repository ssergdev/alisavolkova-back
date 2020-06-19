from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class HeroConfig(AppConfig):
    name = 'hero'
    verbose_name = _('Hero')
