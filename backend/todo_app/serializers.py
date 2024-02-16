from rest_framework import serializers
from todo_app.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    """
    Serializer for the Todo model.
    Serializes Todo model instances to JSON format and vice versa.
    Attributes:
        model: A reference to the Todo model.
        fields: Specifies all fields of the Todo model to be included in the serializer.
        extra_kwargs: Specifies additional options for the serializer fields.
    Note:
        The 'author' field is marked as write-only to prevent it from being included in responses.
    """
    class Meta:
        model = Todo
        fields = '__all__'
        extra_kwargs = {
            'author': {'write_only': True},
        }



class TodoUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for updating Todo model instances.
    Serializes Todo model instances for updating, excluding the 'author' field.
    Attributes:
        model: A reference to the Todo model.
        exclude: Specifies fields of the Todo model to be excluded from the serializer.
    Note:
        The 'author' field is excluded to prevent it from being updated.
    """
    class Meta:
        model = Todo
        exclude = ('author', )
