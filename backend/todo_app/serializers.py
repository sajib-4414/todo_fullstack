from django.contrib.auth.models import Group, User
from rest_framework import serializers
from todo_app.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
