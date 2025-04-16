from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductCombinedViewSet

router = DefaultRouter()
router.register(r'products', ProductCombinedViewSet, basename='product')

urlpatterns = [
    path('api/', include(router.urls)),
]
