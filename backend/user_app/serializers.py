from django.contrib.auth.models import  User
from rest_framework import serializers
from django.contrib.auth.models import User


"""
For Registering user
"""
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.CharField(required=True)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('username', 'email', 'password')