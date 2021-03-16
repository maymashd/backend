import datetime

from django.utils import timezone
from rest_framework import serializers

from OAuth.OAuth.models import MyUser


class UserShortSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(write_only=True)
    is_staff = serializers.BooleanField(read_only=True)

    class Meta:
        model = MyUser
        fields = ('id', 'username', 'first_name', 'last_name',  'password',)


    def create(self, validated_data):
        user = MyUser.objects.create_user(username=validated_data['username'],
                                          first_name=validated_data.get('first_name', ''),
                                          last_name=validated_data.get('last_name', ''),
                                          address=validated_data.get('address', ''),
                                          birth_date=validated_data.get('birth_date', "1999-07-04"))
        print(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user