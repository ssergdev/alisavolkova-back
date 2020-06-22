from django.contrib import admin
from parler.admin import TranslatableAdmin
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from core.admin.decorators import thumbnail
from .models import Event, Photo


@thumbnail('image')
class PhotoInline(SortableInlineAdminMixin, admin.TabularInline):
    classes = ['collapse']
    fields = ['image_thumbnail', 'image']
    extra = 0
    model = Photo


@thumbnail('image')
class EventAdmin(SortableAdminMixin, TranslatableAdmin):
    search_fields = ['translations__name', 'translations__place']
    list_display = ['image_thumbnail', 'name', 'date_start', 'date_end', 'active', 'ordering']
    list_display_links = ['image_thumbnail', 'name']
    list_editable = ['active']
    list_filter = ['date_start', 'date_end', 'active']
    fields = ['image', 'name', 'description', 'place', 'date_start',
              'date_end', 'text', 'artworks', 'slug', 'active']
    inlines = [PhotoInline]
    autocomplete_fields = ['artworks']

    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ['name']
        }


admin.site.register(Event, EventAdmin)
