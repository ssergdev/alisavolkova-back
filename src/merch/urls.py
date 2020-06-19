from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, TagViewSet


app_name = "merch"
router = DefaultRouter()
router.register(r"products", ProductViewSet)
router.register(r"tags", TagViewSet)

urlpatterns = [
    path("", include(router.urls))
]
