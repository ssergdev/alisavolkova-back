from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from core.mixins import PaginationViewMixin, MultipleSerializersMixin
from .models import Product, Tag
from .serializers import ProductSerializer, ProductDetailSerializer, TagSerializer


class ProductViewSet(PaginationViewMixin, MultipleSerializersMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.filter(active=True)
    serializer_class = ProductSerializer
    retrieve_serializer_class = ProductDetailSerializer
    lookup_field = "slug"
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["tags__slug"]


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer




