from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny

from OAuth.service.models import MyUser
from OAuth.service.serializer import UserShortSerializer, UserListSerializer
from rest_framework import mixins,viewsets
from django.http import Http404
from django.http import HttpResponseForbidden
from rest_framework import status
from rest_framework.views import APIView,Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission, AllowAny
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer

class UserCreateView(generics.CreateAPIView):

    permission_classes = (AllowAny, )
    authentication_classes = ()

    def get_queryset(self):
        return MyUser.objects.all()

    def get_serializer_class(self):
        return UserShortSerializer

class Validation(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return MyUser.objects.all()
    def get_serializer_class(self):
        return UserShortSerializer

    def get(self, request, *args, **kwargs):
        if request.user!='':
            return Response(request.user.id)


class is_valid_jwt(mixins.ListModelMixin,
            generics.GenericAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserShortSerializer





def validateUser(token):
    try:
        data = {'token': token}
        valid_data = VerifyJSONWebTokenSerializer().validate(data)
        user = valid_data['user']

        return user.id
    except ValidationError as v:
        return "validation error"



class UserListView(mixins.ListModelMixin,
                    viewsets.GenericViewSet,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.RetrieveModelMixin):

    queryset = MyUser.objects.all()


    def get_serializer_class(self):
        if self.action=='list' :
            return UserListSerializer
        else:
            return UserShortSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'list':
            permission_classes = [IsAdminUser, ]
        else:
            permission_classes = [IsAuthenticated, ]
        return [permission() for permission in permission_classes]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        print(kwargs['pk'])
        print(request.user.id)
        if kwargs['pk'] == str(request.user.id):
            return Response(serializer.data)
        else:
            return HttpResponseForbidden()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if kwargs['pk'] == str(request.user.id):
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return HttpResponseForbidden()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        if kwargs['pk'] == str(request.user.id):
            self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        if kwargs['pk'] == str(request.user.id):
            return Response(serializer.data)
        else:
            return HttpResponseForbidden()

