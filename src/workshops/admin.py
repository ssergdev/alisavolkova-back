from django.contrib import admin
from parler.admin import TranslatableAdmin
from adminsortable2.admin import  SortableInlineAdminMixin
from core.admin.decorators import thumbnail
from .models import Workshop, Photo


@thumbnail('image')
class PhotoInline(SortableInlineAdminMixin, admin.TabularInline):
    classes = ['collapse']
    fields = ['image_thumbnail', 'image']
    extra = 0
    model = Photo


@thumbnail('image')
class WorkshopAdmin(TranslatableAdmin):
    search_fields = ['translations__name', 'translations__place']
    list_display = ['image_thumbnail', 'name',
                    'date_start', 'date_end', 'active']
    list_display_links = ['image_thumbnail', 'name']
    list_editable = ['active']
    fields = ['image', 'name', 'description', 'place',
              'date_start', 'date_end', 'text', 'slug', 'active']
    inlines = [PhotoInline]
    list_filter = ['active', 'date_start']

    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ['name']
        }

admin.site.register(Workshop, WorkshopAdmin)
