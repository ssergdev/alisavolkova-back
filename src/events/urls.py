from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import EventViewSet


app_name = 'events'
router = DefaultRouter()
router.register(r'', EventViewSet)

urlpatterns = [
    path('', include(router.urls))
]
