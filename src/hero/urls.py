from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import SlideViewSet


app_name = 'Hero'
router = DefaultRouter()
router.register(r'', SlideViewSet)

urlpatterns = [
    path('', include(router.urls))
]
