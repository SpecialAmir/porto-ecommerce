from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, CustomerViewSet, CategoryViewSet, OrderViewSet

router = DefaultRouter()
router.register('product',ProductViewSet)
router.register('customer',CustomerViewSet)
router.register('category',CategoryViewSet)
router.register('order',OrderViewSet)

urlpatterns = router.urls
