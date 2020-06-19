from rest_framework import serializers
from core.mixins import ExtraFieldsSerializerMixin
from core.utils import responsiveImage
from .models import Slide


class SlideSerializer(ExtraFieldsSerializerMixin, serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Slide
        fields = '__all__'
        extra_fields = ['text']

    def get_image(self, obj):
        return responsiveImage(obj.image, (468, 768, 990, 1400, 2000))
