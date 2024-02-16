from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from todo_app.models import Todo

class TodoAPIBasicCrudTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_todo_api(self):
        # Test GET request
        response = self.client.get('/todos/')
        self.assertEqual(response.status_code, 200)

        # Test POST request
        data = {'title': 'New Todo', 'description': 'New Description'}
        response = self.client.post('/todos/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Todo.objects.count(), 1)

        # Test PUT request
        todo_id = response.data['id']
        updated_data = {'title': 'Updated Todo', 'description': 'Updated Description'}
        response = self.client.put(f'/todos/{todo_id}/', updated_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Todo.objects.get().title, 'Updated Todo')

        # Test DELETE request
        response = self.client.delete(f'/todos/{todo_id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Todo.objects.count(), 0)
        
class TodoListGetCreateViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_get_todos_list(self):
        Todo.objects.create(title='Test Todo 1', description='Description 1', author=self.user)
        Todo.objects.create(title='Test Todo 2', description='Description 2', author=self.user)
        
        response = self.client.get('/todos/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_create_todo(self):
        data = {'title': 'New Todo', 'description': 'New Description'}
        response = self.client.post('/todos/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertEqual(Todo.objects.get().title, 'New Todo')

class TodoDetailUpdateDeleteViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.todo = Todo.objects.create(title='Test Todo', description='Description', author=self.user)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_get_todo_detail(self):
        response = self.client.get(f'/todos/{self.todo.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Test Todo')

    def test_update_todo(self):
        data = {'title': 'Updated Todo', 'description': 'Updated Description'}
        response = self.client.put(f'/todos/{self.todo.id}/', data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Todo.objects.get().title, 'Updated Todo')

    def test_delete_todo(self):
        response = self.client.delete(f'/todos/{self.todo.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Todo.objects.count(), 0)
