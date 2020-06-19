from rest_framework import serializers
from djmoney.contrib.django_rest_framework import MoneyField
from core.mixins import ExtraFieldsSerializerMixin
from core.utils import responsiveImage
from .models import Tag, Product, Photo


class TagSerializer(ExtraFieldsSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
        extra_fields = ["name"]


class PhotoSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Photo
        fields = "__all__"

    def get_image(self, obj):
        return responsiveImage(obj.image, (468, 768, 990, 1400))


class ProductSerializer(ExtraFieldsSerializerMixin, serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    price = MoneyField(max_digits=14, decimal_places=0)
    tags = TagSerializer(many=True)

    class Meta:
        model = Product
        fields = "__all__"
        extra_fields = ["name", "description"]

    def get_image(self, obj):
        return responsiveImage(obj.image, (468, 768, 990, 1400))


class ProductDetailSerializer(ProductSerializer):
    photos = PhotoSerializer(many=True, read_only=True)
    related = serializers.SerializerMethodField()

    def get_related(self, obj):
        return []
