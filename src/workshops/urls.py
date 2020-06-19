from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import WorkshopViewSet


app_name = "workshops"
router = DefaultRouter()
router.register(r"", WorkshopViewSet)

urlpatterns = [
    path("", include(router.urls))
]
