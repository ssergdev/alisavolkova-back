from django.utils.html import mark_safe
from django.utils.translation import ugettext_lazy as _
from easy_thumbnails.files import get_thumbnailer


def thumbnail(field_name, *args, **kwargs):
    def _wrapper(admin_class):
        def thumbnail_field(self, obj):
            field = obj._meta.get_field(field_name)
            field_value = getattr(obj, field_name)
            if not field_value:
                return ''

            thumbnailer = get_thumbnailer(field_value)
            thumbnail = thumbnailer.get_thumbnail({'size': (80, 0)})
            return mark_safe('<img src="%s" />' % (thumbnail.url))

        thumbnail_field.short_description = _('Preview')
        new_field_name = '{0}_thumbnail'.format(field_name)
        setattr(admin_class, new_field_name, thumbnail_field)
        admin_class.readonly_fields = admin_class.readonly_fields + \
            (new_field_name,)
        return admin_class

    return _wrapper
