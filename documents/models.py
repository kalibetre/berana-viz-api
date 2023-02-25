import uuid

from django.db import models


class Document(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    version = models.IntegerField(default=1)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    content = models.JSONField(blank=True)
    is_published = models.BooleanField(default=False)
    shared_at = models.DateTimeField(null=True)
    last_modified = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
