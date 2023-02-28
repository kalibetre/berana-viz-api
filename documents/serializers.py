from rest_framework.serializers import ModelSerializer

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
