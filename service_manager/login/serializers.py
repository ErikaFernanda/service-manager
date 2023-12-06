from rest_framework import serializers
from .models import User

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