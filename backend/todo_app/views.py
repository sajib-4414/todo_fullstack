from todo_app.models import Todo
from todo_app.serializers import TodoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
"""
For creating a new Todo and listing all todos of a user
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