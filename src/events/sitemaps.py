from django.contrib.sitemaps import Sitemap
from django.utils import translation
from .models import Event


class EventsSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8
    i18n = True

    def items(self):
        return Event.objects.filter()

    def location(self, obj):
        return '/%s/events/%s' % (obj.get_current_language(), obj.slug)

    def lastmod(self, obj):
        return obj.created
