from rest_framework.viewsets import ModelViewSet

from .models import Document
from .serializer import DocumentSerializer


class DocumentViewSet(ModelViewSet):
    """
    A viewset that provides `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions for Document instances
    """
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
    lookup_field = "uid"

    def get_serializer_context(self):
        return {'request': self.request}
