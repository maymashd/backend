from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    address = models.CharField(max_length=50, default='')
    middle_name=models.CharField(max_length=50,default='')
    birth_date = models.DateField(null=True, blank=True)
    def __str__(self):
        return 'username: {}, Full name: {}'.format(self.username, self.get_full_name())