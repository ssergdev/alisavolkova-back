from django.utils.html import linebreaks
from rest_framework import serializers
from core.mixins import ExtraFieldsSerializerMixin
from core.utils import responsiveImage
from .models import Artwork, Tag, Photo


class TagSerializer(ExtraFieldsSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        extra_fields = ['name', 'description']


class PhotoSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Photo
        fields = '__all__'

    def get_image(self, obj):
        return responsiveImage(obj.image, (768, 990, 1400))


class ArtworkSerializer(ExtraFieldsSerializerMixin, serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    image = serializers.SerializerMethodField()

    class Meta:
        model = Artwork
        fields = '__all__'
        extra_fields = ['name', 'description', 'text', 'history']
    
    def get_image(self, obj):
        return responsiveImage(obj.image, (468, 768, 990, 1400))


class ArtworkDetailSerializer(ArtworkSerializer):
    photos = PhotoSerializer(many=True, read_only=True)
    related = ArtworkSerializer(many=True)
    description = serializers.SerializerMethodField()

    class Meta:
        model = Artwork
        fields = '__all__'
        extra_fields = ['name', 'description', 'text', 'history']

    def get_description(self, obj):
        return linebreaks(obj.description)
