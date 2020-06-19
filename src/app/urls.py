from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from .sitemaps import sitemaps


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/gallery/', include('gallery.urls')),
    path('api/v1/blocks/', include('blocks.urls')),
    path('api/v1/hero/', include('hero.urls')),
    path('api/v1/events/', include('events.urls')),
    path('api/v1/workshops/', include('workshops.urls')),
    path('api/v1/merch/', include('merch.urls')),
    path('api/v1/feedback/', include('feedback.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
]
