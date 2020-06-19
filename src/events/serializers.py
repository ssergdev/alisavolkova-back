from rest_framework import serializers
from core.mixins import ExtraFieldsSerializerMixin
from core.utils import responsiveImage
from gallery.serializers import ArtworkSerializer
from .models import Event, Photo


class PhotoSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Photo
        fields = '__all__'

    def get_image(self, obj):
        return responsiveImage(obj.image, (768, 990, 1400))


class EventSerializer(ExtraFieldsSerializerMixin, serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = '__all__'
        extra_fields = ['name', 'description', 'place']

    def get_image(self, obj):
        return responsiveImage(obj.image, (468, 768, 990, 1400))


class EventDetailSerializer(EventSerializer):
    artworks = ArtworkSerializer(many=True)
    photos = PhotoSerializer(many=True)

    class Meta:
        model = Event
        fields = '__all__'
        extra_fields = ['name', 'description', 'text', 'place']
