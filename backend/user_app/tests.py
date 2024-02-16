from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

class TestUserViews(APITestCase):
    """
    Test case for testing user-related views such as registration, login, user list, and user deletion.
    Attributes:
        admin_user: A superuser instance created for testing administrative tasks.
        user: A regular user instance created for testing user-related views.
        client: An instance of APIClient for making API requests.

    Methods:
        setUp: Setup method to create test users and authenticate the client.
        test_register_view: Method to test user registration view.
        test_login_view: Method to test user login view.
        test_user_list_view: Method to test user list view.
        test_user_delete_view: Method to test user deletion view.
        test_user_delete_view_cannot_delete_self: Method to test user deletion view when attempting to delete oneself.
    """
    
    
    
    def setUp(self):
        """Setup method to create test users and authenticate the client."""
        self.admin_user = User.objects.create_superuser(username='admin', email='admin@example.com', password='adminpassword')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.client.force_authenticate(user=self.admin_user)

    def test_register_view(self):
        """Method to test user registration view."""
        data = {'username': 'newuser', 'email': 'newuser@example.com', 'password': 'newpassword', 'confirmPassword': 'newpassword'}
        response = self.client.post('/auth/register/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', response.data)
        self.assertIn('user', response.data)
        self.assertEqual(response.data['user']['username'], 'newuser')
        self.assertEqual(response.data['user']['email'], 'newuser@example.com')
        self.assertIn('superuser_status', response.data['user'])

    def test_login_view(self):
        """Method to test user login view."""
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post('/auth/login/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)
        self.assertIn('user', response.data)
        self.assertEqual(response.data['user']['username'], 'testuser')
        self.assertEqual(response.data['user']['email'], 'test@example.com')
        self.assertIn('superuser_status', response.data['user'])

    def test_user_list_view(self):
        """Method to test user list view."""
        response = self.client.get('/auth/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_user_delete_view(self):
        """Method to test user deletion view."""
        response = self.client.delete(f'/auth/users/{self.user.username}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_delete_view_cannot_delete_self(self):
        """Method to test user deletion view when attempting to delete oneself."""
        response = self.client.delete(f'/auth/users/{self.admin_user.username}/')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('You cannot delete yourself.', response.data['message'])
