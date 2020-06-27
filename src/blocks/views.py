from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from .models import Block
from .serializers import BlockSerializer


class BlockViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer
    filter_backends = [SearchFilter]
    search_fields = ['^slug']
    lookup_field = 'slug'
