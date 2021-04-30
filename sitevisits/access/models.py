from django.db import models
from django.contrib.auth.models import AbstractUser
from sitevisits.common.models import UUIDTimeStamp

class User(AbstractUser, UUIDTimeStamp):
    def __str__(self):
        return self.first_name
