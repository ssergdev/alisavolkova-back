from datetime import date
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter
from core.mixins import PaginationViewMixin
from .models import Event
from .serializers import EventSerializer, EventDetailSerializer


def _filter_time(queryset, value):
    today = date.today()
    if value:
        if value == 'present':
            queryset = queryset.filter(date_start__lte=today)
            queryset = queryset.filter(
                date_end__gte=today) | queryset.filter(date_end__isnull=True)
        elif value == 'upcoming':
            queryset = queryset.filter(date_start__gt=today)
        elif value == 'past':
            queryset = queryset.filter(date_end__lt=today)
        else:
            queryset = queryset.none()

    return queryset


class EventsFilter(FilterSet):
    time = CharFilter(method='filter_time')

    class Meta:
        model = Event
        fields = ['time']

    def filter_time(self, queryset, name, value):
        return _filter_time(queryset, value)


class EventViewSet(PaginationViewMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Event.objects.filter(active=True)
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_class = EventsFilter

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return EventDetailSerializer
        else:
            return EventSerializer

    @action(detail=False)
    def total(self, request):
        present_queryset = _filter_time(self.queryset, 'present')
        upcoming_queryset = _filter_time(self.queryset, 'upcoming')
        past_queryset = _filter_time(self.queryset, 'past')

        return Response({
            'present': present_queryset.count(),
            'upcoming': upcoming_queryset.count(),
            'past': past_queryset.count()
        })
