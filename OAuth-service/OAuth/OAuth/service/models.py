from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    address=models.CharField(default='',max_length=50)
    def __str__(self):
        return 'username: {}'.format(self.username)