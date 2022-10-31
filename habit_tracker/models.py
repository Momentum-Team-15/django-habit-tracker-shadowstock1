from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import DateTimeField

# Create your models here.

class User(AbstractUser):
    pass
