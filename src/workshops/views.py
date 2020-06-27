from rest_framework import viewsets
from core.mixins import PaginationViewMixin, MultipleSerializersMixin
from .models import Workshop
from .serializers import WorkshopSerializer, WorkshopDetailSerializer


class WorkshopViewSet(MultipleSerializersMixin, PaginationViewMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Workshop.objects.filter(active=True)
    lookup_field = 'slug'
    serializer_class = WorkshopSerializer
    retrieve_serializer_class = WorkshopDetailSerializer
