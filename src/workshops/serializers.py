from rest_framework import serializers
from core.mixins import ExtraFieldsSerializerMixin
from core.utils import responsiveImage
from .models import Workshop, Photo


class PhotoSerialzier(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Photo
        fields = "__all__"

    def get_image(self, obj):
        return responsiveImage(obj.image, (768, 990, 1400))


class WorkshopSerializer(ExtraFieldsSerializerMixin, serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Workshop
        fields = "__all__"
        extra_fields = ["name", "description", "text", "place"]

    def get_image(self, obj):
        return responsiveImage(obj.image, (468, 768, 990, 1400))


class WorkshopDetailSerializer(WorkshopSerializer):
    image = serializers.SerializerMethodField()
    photos = PhotoSerialzier(many=True)
