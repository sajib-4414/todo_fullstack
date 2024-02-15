from django.db import models
from django.contrib.auth.models import User

# Todo Model that will store each todo with the ORM to database
class Todo(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    done = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #on delete of author, delete the todos
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)