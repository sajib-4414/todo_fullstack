from django.contrib.auth.models import User
from user_app.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class RegisterView(APIView):
    """
    API view for user registration.
    Attributes:
        None
    Methods:
        post: Method to handle user registration.
    """
    
    
    def post(self, request):
        """Method to handle user registration."""
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            token_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            response_data = {
                'user': {
                    'username': user.username,
                    'email': user.email,
                    'superuser_status': user.is_superuser  # Include superuser status
                },
                'token': token_data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LoginView(TokenObtainPairView):
    """
    API view for user login.
    Attributes:
        None
    Methods:
        post: Method to handle user login.
    """
    
    
    def post(self, request, *args, **kwargs):
        """Method to handle user login."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.user
        refresh = RefreshToken.for_user(user) 
        access = refresh.access_token

        return Response({
            'user': {
                'username': user.username,
                'email': user.email,
                'superuser_status': user.is_superuser  # Include superuser status
            },
            'token': {
                'refresh': str(refresh),
                'access': str(access),
            }
        })


class UserListView(generics.ListAPIView):
    """
    API view for listing all users (only available to admin users).
    Attributes:
        queryset: A queryset containing all User instances.
        serializer_class: The serializer class to use for User instances.
        permission_classes: A list of permission classes applied to the view.
        
    Methods:
        list: Method to retrieve a list of all users.
    """
    
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def list(self, request, *args, **kwargs):
        """Method to retrieve a list of all users."""
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



class UserDeleteView(generics.DestroyAPIView):
    """
    API view for deleting a user (only available to admin users).
    Attributes:
        queryset: A queryset containing all User instances.
        permission_classes: A list of permission classes applied to the view.

    Methods:
        destroy: Method to handle deletion of a user.
    """
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]

    def destroy(self, request, *args, **kwargs):
        """Method to handle deletion of a user."""
        username = self.kwargs.get('username')
        
        if request.user.username == username:
            return Response({'message': 'You cannot delete yourself.'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = self.get_queryset().get(username=username)
        except User.DoesNotExist:
            return Response({'message': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        user.delete()

        return Response({'message': f'User {username} has been deleted.'}, status=status.HTTP_204_NO_CONTENT)
