from django.db import models
from sitevisits.common.models import UUIDTimeStamp
from sitevisits.access.models import User
import uuid

class Account(UUIDTimeStamp):
    key = models.UUIDField(default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    visits = models.IntegerField(default=0)
    author = models.ForeignKey(User,
                               related_name='accounts',
                               on_delete=models.CASCADE)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['author', 'title'],
                                    name='unique together constraint')
        ]
        ordering = ('visits', 'title')
    
    def __str__(self):
        return title