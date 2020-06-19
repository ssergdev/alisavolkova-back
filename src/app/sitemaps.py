from django.contrib.sitemaps import Sitemap
from django.utils import translation
from events.sitemaps import EventsSitemap
from gallery.sitemaps import ArtworksSitemap
from workshops.sitemaps import WorkshopsSitemap
from merch.sitemaps import ProductsSitemap


class StaticSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1
    i18n = True

    def items(self):
        return ['', 'gallery', 'events', 'workshops', 'merch', 'about', 'contacts']

    def location(self, item):
        path = f"/{translation.get_language()}"
        if item == '':
            return path
        path = path + f"/{item}"
        return path


sitemaps = {
    'static': StaticSitemap,
    'events': EventsSitemap,
    'products': ProductsSitemap,
    'artworks': ArtworksSitemap,
    'workshops': WorkshopsSitemap
}
