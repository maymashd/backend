from rest_framework import generics
from rest_framework.permissions import AllowAny

from OAuth.service.models import MyUser
from OAuth.service.serializer import UserShortSerializer
from rest_framework import mixins,viewsets
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView,Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission, AllowAny

class UserCreateView(generics.CreateAPIView):

    permission_classes = (AllowAny, )
    authentication_classes = ()

    def get_queryset(self):
        return MyUser.objects.all()

    def get_serializer_class(self):
        return UserShortSerializer



class UserListView(mixins.ListModelMixin,
                    viewsets.GenericViewSet,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.RetrieveModelMixin):

    queryset = MyUser.objects.all()
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        return UserShortSerializer
    def get_permissions(self):
        if self.request.method=='GET':
            self.permission_classes = [IsAdminUser,IsAuthenticated,]
        else:
            self.permission_classes=[IsAuthenticated,]