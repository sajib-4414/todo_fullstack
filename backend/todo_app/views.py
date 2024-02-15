from todo_app.models import Todo
from todo_app.serializers import TodoSerializer, TodoUpdateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.http import Http404
"""
For creating a new Todo and listing all todos of an authenticated user
"""
class TodoListGetCreateView(APIView):
    permission_classes = [IsAuthenticated]
    
    """
    Returns list of todos owned by the logged in user
    """
    def get(self, request):
        todos = Todo.objects.filter(author=request.user)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        payload = request.data.copy()
        payload['author'] = request.user.id
        serializer = TodoSerializer(data=payload)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoDetailUpdateDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get_object(self, pk):
        try:
            return Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        todo = self.get_object(pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    
    def put(self, request, pk):
        todo = self.get_object(pk)
        serializer = TodoUpdateSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        todo = self.get_object(pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
