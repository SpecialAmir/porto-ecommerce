from rest_framework.routers import DefaultRouter

from .views import (
        ProductViewSet, CustomerViewSet, CategoryViewSet, OrderViewSet, UserViewSet
        )

router = DefaultRouter()
router.register('product',ProductViewSet)
router.register('customer',CustomerViewSet)
router.register('category',CategoryViewSet)
router.register('order',OrderViewSet)
router.register('user',UserViewSet)

urlpatterns = router.urls
