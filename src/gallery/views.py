from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from core.mixins import PaginationViewMixin, MultipleSerializersMixin
from .models import Artwork, Tag
from .serializers import TagSerializer, ArtworkSerializer, ArtworkDetailSerializer


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ArtworkViewSet(PaginationViewMixin, MultipleSerializersMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Artwork.objects.filter(active=True)
    serializer_class = ArtworkSerializer
    retrieve_serializer_class = ArtworkDetailSerializer
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['tags__slug']
    ordering_fields = ['promote', 'ordering', 'created']
    search_fields = ['translations__name',
                     'translations__description', 'tags__translations__name']
