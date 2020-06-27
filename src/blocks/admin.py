from django import forms
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from parler.forms import TranslatableModelForm
from parler.admin import TranslatableAdmin, TranslatableTabularInline, SortedRelatedFieldListFilter
from .models import Block


class BlockAdminForm(TranslatableModelForm):
    class Meta:
        model = Block
        fields = ['slug', 'type', 'text', 'image']

    def clean_type(self):
        type = self.cleaned_data['type']
        if self.instance.pk and self.instance.type != type:
            raise forms.ValidationError(
                _("Sorry, you can't change the type of existing block"))
        return type


class BlockAdmin(TranslatableAdmin):
    list_display = ['slug', 'type', 'created', 'modified']
    list_display_links = ['type', 'slug']
    search_fields = ['slug']
    list_filter = ['type']
    form = BlockAdminForm

    class Media:
        js = ['admin/js/related_fields.js']


admin.site.register(Block, BlockAdmin)
