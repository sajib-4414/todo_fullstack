from todo_app.models import Todo
from todo_app.serializers import TodoSerializer, TodoUpdateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.http import Http404

class TodoListGetCreateView(APIView):
    """
    API view for creating a new Todo and listing all todos of an authenticated user.
    Attributes:
        permission_classes: A list of permission classes applied to the view.
    Methods:
        get: Method to retrieve a list of todos owned by the logged-in user.
        post: Method to create a new Todo for the logged-in user.
    """
    
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        """Returns a list of todos owned by the logged-in user."""
        todos = Todo.objects.filter(author=request.user)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """Creates a new Todo for the logged-in user."""
        payload = request.data.copy()
        payload['author'] = request.user.id
        serializer = TodoSerializer(data=payload)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoDetailUpdateDeleteView(APIView):
    """
    API view for updating and deleting todos owned by the logged-in user.
    
    Attributes:
        permission_classes: A list of permission classes applied to the view.

    Methods:
        get_object: Helper method to retrieve a Todo object by its primary key.
        get: Method to retrieve details of a specific Todo.
        put: Method to update a specific Todo.
        delete: Method to delete a specific Todo.
    """
    
    
    permission_classes = [IsAuthenticated]
    
    def get_object(self, pk):
        """Helper method to retrieve a Todo object by its primary key."""
        try:
            return Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        """Retrieves details of a specific Todo."""
        todo = self.get_object(pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    
    def put(self, request, pk):
        """Updates a specific Todo."""
        todo = self.get_object(pk)
        serializer = TodoUpdateSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        """Deletes a specific Todo."""
        todo = self.get_object(pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
