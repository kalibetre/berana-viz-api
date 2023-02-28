from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from .models import User
from .serializers import UserSerializer


class UserViewSet(CreateModelMixin, RetrieveModelMixin, GenericViewSet):
    """
    A viewset that provides `create()`, `retrieve()`, actions for User
    instances
    """
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()

    def perform_create(self, serializer):
        pass

    def get_serializer_context(self):
        return {'request': self.request}
