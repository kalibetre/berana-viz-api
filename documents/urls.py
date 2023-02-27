from rest_framework.routers import SimpleRouter

from .views import DocumentOwnerViewSet, DocumentViewSet

router = SimpleRouter()
router.register('documents', DocumentViewSet)
router.register('users', DocumentOwnerViewSet)

urlpatterns = router.urls
