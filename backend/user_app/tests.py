from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

class TestUserViews(APITestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser(username='admin', email='admin@example.com', password='adminpassword')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.client.force_authenticate(user=self.admin_user)

    def test_register_view(self):
        data = {'username': 'newuser', 'email': 'newuser@example.com', 'password': 'newpassword', 'confirmPassword': 'newpassword'}
        response = self.client.post('/auth/register/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', response.data)
        self.assertIn('user', response.data)
        self.assertEqual(response.data['user']['username'], 'newuser')
        self.assertEqual(response.data['user']['email'], 'newuser@example.com')
        self.assertIn('superuser_status', response.data['user'])

    def test_login_view(self):
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post('/auth/login/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)
        self.assertIn('user', response.data)
        self.assertEqual(response.data['user']['username'], 'testuser')
        self.assertEqual(response.data['user']['email'], 'test@example.com')
        self.assertIn('superuser_status', response.data['user'])

    def test_user_list_view(self):
        response = self.client.get('/auth/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_user_delete_view(self):
        response = self.client.delete(f'/auth/users/{self.user.username}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_delete_view_cannot_delete_self(self):
        response = self.client.delete(f'/auth/users/{self.admin_user.username}/')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('You cannot delete yourself.', response.data['message'])
