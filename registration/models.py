from django.db import models
from django.contrib.auth.models import AbstractUser

from registration.definition import Gender

# Create your models here.


class User(AbstractUser):
    photo = models.ImageField(upload_to='photos', null=True, blank=True)
    introduction = models.TextField(null=True, blank=True)
    email_is_verified = models.BooleanField(default=False)
    gender = models.SmallIntegerField(default=Gender.Unset.value[0])
