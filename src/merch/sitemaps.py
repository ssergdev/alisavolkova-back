from django.contrib.sitemaps import Sitemap
from django.utils import translation
from .models import Product


class ProductsSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8
    i18n = True

    def items(self):
        return Product.objects.filter()

    def location(self, obj):
        return '/%s/merch/%s' % (obj.get_current_language(), obj.slug)

    def lastmod(self, obj):
        return obj.created
