from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from todo_app.models import Todo

class TodoAPIBasicCrudTestCase(TestCase):
    """
    Test case for testing basic CRUD operations on the Todo API.
    Attributes:
        user: A test user created for authentication.
        client: An instance of APIClient for making API requests.
        
    Methods:
        setUp: Setup method to create a test user and authenticate the client.
        test_todo_api: Method to test GET, POST, PUT, and DELETE requests on the Todo API.
    """
    
    
    def setUp(self):
        """Setup method to create a test user and authenticate the client."""
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_todo_api(self):
        """Method to test GET, POST, PUT, and DELETE requests on the Todo API."""
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
    """
    Test case for testing Todo list retrieval and creation views.
    Attributes:
        user: A test user created for authentication.
        client: An instance of APIClient for making API requests.
        
    Methods:
        setUp: Setup method to create a test user and authenticate the client.
        test_get_todos_list: Method to test retrieval of the Todo list.
        test_create_todo: Method to test creation of a new Todo item.
    """
    
    
    def setUp(self):
        """Setup method to create a test user and authenticate the client."""
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_get_todos_list(self):
        """Method to test retrieval of the Todo list."""
        Todo.objects.create(title='Test Todo 1', description='Description 1', author=self.user)
        Todo.objects.create(title='Test Todo 2', description='Description 2', author=self.user)
        
        response = self.client.get('/todos/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_create_todo(self):
        """Method to test creation of a new Todo item."""
        data = {'title': 'New Todo', 'description': 'New Description'}
        response = self.client.post('/todos/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertEqual(Todo.objects.get().title, 'New Todo')

class TodoDetailUpdateDeleteViewTestCase(TestCase):
    """
    Test case for testing Todo detail retrieval, update, and deletion views.
    Attributes:
        user: A test user created for authentication.
        todo: A test Todo item created for testing detail, update, and deletion views.
        client: An instance of APIClient for making API requests.

    Methods:
        setUp: Setup method to create a test user, a test Todo item, and authenticate the client.
        test_get_todo_detail: Method to test retrieval of the Todo item detail.
        test_update_todo: Method to test update of the Todo item.
        test_delete_todo: Method to test deletion of the Todo item.
    """
    
    
    def setUp(self):
        """Setup method to create a test user, a test Todo item, and authenticate the client."""
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.todo = Todo.objects.create(title='Test Todo', description='Description', author=self.user)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_get_todo_detail(self):
        """Method to test retrieval of the Todo item detail."""
        response = self.client.get(f'/todos/{self.todo.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Test Todo')

    def test_update_todo(self):
        """Method to test update of the Todo item."""
        data = {'title': 'Updated Todo', 'description': 'Updated Description'}
        response = self.client.put(f'/todos/{self.todo.id}/', data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Todo.objects.get().title, 'Updated Todo')

    def test_delete_todo(self):
        """Method to test deletion of the Todo item."""
        response = self.client.delete(f'/todos/{self.todo.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Todo.objects.count(), 0)
