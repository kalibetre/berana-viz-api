import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """User model

    Args:
        AbstractUser : default Django user
    """
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    auth_id = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
