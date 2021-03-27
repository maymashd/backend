from rest_framework import serializers

from OAuth.service.models import MyUser


class UserShortSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = MyUser
        fields = ('id', 'username', 'first_name', 'last_name', 'password',)

    def create(self, validated_data):
        user = MyUser.objects.create_user(username=validated_data['username'],
                                          )
        print(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserListSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)
    username=serializers.CharField(read_only=True)


    class Meta:
        model=MyUser
        fields=('id','username',)