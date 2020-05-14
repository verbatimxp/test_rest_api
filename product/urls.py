from rest_framework.routers import DefaultRouter

from .views import ProductGroupViewSet, ProductViewSet

router = DefaultRouter()
router.register('product', ProductViewSet)
router.register('product_group', ProductGroupViewSet)

urlpatterns = router.urls
