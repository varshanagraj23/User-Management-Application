from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),          # List all users
    path('create/', views.user_create, name='user_create'), # Create a new user
    path('<int:pk>/update/', views.user_update, name='user_update'), # Update an existing user
    path('<int:pk>/delete/', views.user_delete, name='user_delete'), # Delete a user
]
