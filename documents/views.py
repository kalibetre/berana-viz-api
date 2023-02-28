from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from documents.permissions import IsOwner

from .models import Document
from .serializers import DocumentSerializer


class DocumentViewSet(ModelViewSet):
    """
    A viewset that provides `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions for Document instances
    """
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Document.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_context(self):
        return {'request': self.request}
