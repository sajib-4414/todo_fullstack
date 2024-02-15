from django.urls import path,include
from todo_app.views import TodoListGetCreateView
urlpatterns = [
    path("", TodoListGetCreateView.as_view(), name='todo-list-create'),
]