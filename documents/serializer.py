from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from core.models import User

from .models import Document


class DocumentSerializer(ModelSerializer):
    """
    A Document Serializer Class that used for serializing and deserializing of
    Document instances
    """

    class Meta:
        model = Document
        fields = ('uid', 'title', 'description', 'modified', 'created',
                  'content')


class DocumentOwnerSerializer(ModelSerializer):
    """
    A Document Owner serializer that is used to retrieve user information
    with related documents
    """
    documents = PrimaryKeyRelatedField(many=True,
                                       queryset=Document.objects.all())

    class Meta:
        model = User
        fields = ('uid', 'email', 'documents')
        read_only_fields = ('uid', 'email')
