from django.contrib import admin
from parler.admin import TranslatableAdmin, TranslatableTabularInline, SortedRelatedFieldListFilter
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from core.admin.decorators import thumbnail
from .models import Artwork, Tag, Photo


@thumbnail('image')
class PhotoInline(SortableInlineAdminMixin, admin.TabularInline):
    classes = ['collapse']
    fields = ['image_thumbnail', 'image']
    extra = 0
    model = Photo


class TagAdmin(SortableAdminMixin, TranslatableAdmin):
    search_fields = ['translations__name']
    list_display = ['name', 'created', 'modified', 'ordering']
    fields = ['name', 'description', 'slug']

    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('name',)
        }


@thumbnail('image')
class ArtworkAdmin(SortableAdminMixin, TranslatableAdmin):
    search_fields = ['translations__name']
    list_display = ['image_thumbnail', 'name', 'created',
                    'modified', 'promote', 'active', 'ordering']
    list_display_links = ['image_thumbnail', 'name']
    list_editable = ['promote', 'active']
    list_filter = (
        ('tags', SortedRelatedFieldListFilter),
        ('promote'),
        ('active')
    )
    inlines = [PhotoInline]
    fields = ['image', 'name', 'description',
              'text', 'history', 'tags', 'slug', 'promote', 'active']
    autocomplete_fields = ['tags']

    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ['name']
        }


admin.site.register(Tag, TagAdmin)
admin.site.register(Artwork, ArtworkAdmin)
