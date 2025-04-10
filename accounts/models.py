from rest_framework.authtoken.models import Token

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    @property
    def token(self):
        token = Token.objects.filter(user=self)
        if token:
            return token.first().key
        token = Token.objects.create(user=self)
        return token.key
