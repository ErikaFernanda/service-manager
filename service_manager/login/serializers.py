from rest_framework import serializers
from .models import User


from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):

        password = validated_data.pop('password', None)
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
    company_id = serializers.IntegerField()


class RedirectSerializer(serializers.Serializer):
    refresh_token = serializers.CharField(max_length=255)
    application_id = serializers.IntegerField()


class RefreshSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()


class IsValidTokenSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    token = serializers.CharField(required=True)
