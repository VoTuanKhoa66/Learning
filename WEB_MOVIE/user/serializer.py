from user.models import UserAcount
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer

class UserAcountSerializer(UserCreateSerializer):
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)
    class Meta(UserCreateSerializer.Meta):
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'phone', 'address')

class UserAcountUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAcount
        fields = ('first_name', 'last_name', 'email', 'phone', 'address')
