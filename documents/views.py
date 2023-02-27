from rest_framework.mixins import RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from core.models import User
from documents.permissions import IsOwner, IsSelf

from .models import Document
from .serializer import DocumentOwnerSerializer, DocumentSerializer


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


class DocumentOwnerViewSet(RetrieveModelMixin, GenericViewSet):
    """
    A viewset that provides `retrieve()` action for a user (document owner)
    instances
    """
    serializer_class = DocumentOwnerSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsSelf]

    def get_serializer_context(self):
        return {'request': self.request}
