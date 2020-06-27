from django.contrib import admin
from parler.admin import TranslatableAdmin
from adminsortable2.admin import SortableAdminMixin
from core.admin.decorators import thumbnail
from .models import Slide


@thumbnail('image')
class SlideAdmin(SortableAdminMixin, TranslatableAdmin):
    list_display = ['image_thumbnail', 'created',
                    'modified', 'active', 'ordering']
    list_filter = ['active']
    list_editable = ['active']
    fields = ['image', 'text', 'active']


admin.site.register(Slide, SlideAdmin)
