from django.contrib.sitemaps import Sitemap
from django.utils import translation
from .models import Artwork


class ArtworksSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8
    i18n = True

    def items(self):
        return Artwork.objects.filter()

    def location(self, obj):
        return '/%s/gallery/%s' % (obj.get_current_language(), obj.slug)

    def lastmod(self, obj):
        return obj.created
