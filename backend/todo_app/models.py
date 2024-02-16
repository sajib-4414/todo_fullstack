from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    """
    Model representing a Todo item.
    Each Todo item consists of a title, description, status (done/not done),
    author (user who created the Todo), creation date, and last update date.
    Attributes:
        title: A character field representing the title of the Todo item.
        description: A text field representing the description of the Todo item.
        done: A boolean field indicating whether the Todo item is completed.
        author: A foreign key field referencing the User model representing the author of the Todo item.
        created_at: A datetime field representing the date and time when the Todo item was created.
        updated_at: A datetime field representing the date and time when the Todo item was last updated.
        
    Note:
        The 'author' field is a foreign key relationship with the User model, indicating that each Todo item
        is associated with a specific user who created it. The 'on_delete=models.CASCADE' option ensures
        that when a user is deleted, all related Todo items are also deleted.
    """
    title = models.CharField(max_length=80)
    description = models.TextField()
    done = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #on delete of author, delete the todos
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)