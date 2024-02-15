from django.urls import path,include
from todo_app.views import TodoListGetCreateView, TodoDetailUpdateDeleteView
urlpatterns = [
    path("", TodoListGetCreateView.as_view(), name='todo-list-create'),
    path('<int:pk>/', TodoDetailUpdateDeleteView.as_view(), name='todo-detail-update-delete'),
]
   