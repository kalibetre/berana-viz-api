from rest_framework.serializers import CharField, ModelSerializer

from .models import User


class UserSerializer(ModelSerializer):
    """
    A User Serializer Class that used for serializing and deserializing of
    User instances
    """
    id = CharField(source='auth_id')

    class Meta:
        model = User
        fields = ('id', 'email')
        read_only_fields = ('id', 'email')
