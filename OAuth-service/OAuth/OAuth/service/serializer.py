from rest_framework import serializers

from OAuth.service.models import MyUser


class UserShortSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = MyUser
        fields = ('id', 'username', 'first_name', 'last_name',  'password','address','birth_date')


