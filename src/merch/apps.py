from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class MerchConfig(AppConfig):
    name = 'merch'
    verbose_name = _('Merch')
