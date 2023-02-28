from rest_framework.routers import SimpleRouter

from .views import DocumentViewSet

router = SimpleRouter()
router.register('documents', DocumentViewSet, basename='documents')

urlpatterns = router.urls
