from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for registering a user.
    Serializes user registration data and creates a new user.
    Attributes:
        password: A write-only field for user password.
        email: A required field for user email.
    Methods:
        create: Method to create a new user using validated data.
    Note:
        This serializer is used for registering a new user.
    """
    
    password = serializers.CharField(write_only=True)
    email = serializers.CharField(required=True)

    def create(self, validated_data):
        """Method to create a new user using validated data."""
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
