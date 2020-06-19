from rest_framework import viewsets
from .models import Slide
from .serializers import SlideSerializer


class SlideViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Slide.objects.filter(active=True)
    serializer_class = SlideSerializer
