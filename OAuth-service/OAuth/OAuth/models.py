from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):

    middle_name=models.CharField(max_length=50,default='')
    def __str__(self):
        return 'username: {}, Full name: {}'.format(self.username, self.get_full_name())