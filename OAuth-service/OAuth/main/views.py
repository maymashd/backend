from rest_framework import generics, mixins, viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from OAuth.OAuth.models import MyUser
from OAuth.OAuth.serializer import UserShortSerializer


class UserCreateView(generics.CreateAPIView):

    permission_classes = (AllowAny, )
    authentication_classes = ()

    def get_queryset(self):
        return MyUser.objects.all()

    def get_serializer_class(self):
        return UserShortSerializer