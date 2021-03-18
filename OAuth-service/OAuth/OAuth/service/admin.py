from django.contrib import admin

# Register your models here.
from django.contrib import admin

from OAuth.service.models import MyUser


class AuthorAdmin(admin.ModelAdmin):
    admin.site.register(MyUser)