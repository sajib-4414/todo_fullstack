from django.contrib.auth.models import Group, User
from rest_framework import serializers
from todo_app.models import Todo
from django.contrib.auth.models import User

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
        extra_kwargs = {
            'author': {'write_only': True},
        }
    
class TodoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        exclude = ('author', )


