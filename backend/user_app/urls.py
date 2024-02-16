from django.urls import path
from user_app.views import  RegisterView,LoginView, UserListView, UserDeleteView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='register'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<str:username>/', UserDeleteView.as_view(), name='user-delete'),
]