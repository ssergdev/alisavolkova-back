from django.contrib import admin
from parler.admin import TranslatableAdmin
from adminsortable2.admin import SortableAdminMixin
from core.admin.decorators import thumbnail
from .models import Slide


@thumbnail('image')
class SlideAdmin(SortableAdminMixin, TranslatableAdmin):
    list_display = ['image_thumbnail', 'created', 'modified', 'active']
    list_filter = ['active']
    fields = ['image', 'text', 'active']


admin.site.register(Slide, SlideAdmin)
