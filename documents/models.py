import uuid

from django.conf import settings
from django.db import models


class Document(models.Model):
    """Document Data Model
    Represents a data structure document that contains all the node values
    as well as additional metadata

    Args:
        models (_type_): _description_
    """
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    version = models.IntegerField(default=1)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    content = models.JSONField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'document'
        verbose_name_plural = "Documents"
        indexes = [models.Index(fields=['title'])]
        ordering = ['modified', 'title']
