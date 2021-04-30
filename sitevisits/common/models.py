from django.db import models
import uuid

# Create your models here.

class UUID(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Timestamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UUIDTimeStamp(UUID, Timestamp):
    pass

    class Meta:
        abstract = True