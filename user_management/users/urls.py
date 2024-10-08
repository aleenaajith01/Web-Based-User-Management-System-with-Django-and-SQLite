# users/urls.py
from django.urls import path
from .views import create_user, list_users, edit_user, update_user, delete_user  # Ensure delete_user is imported
from .views import saveEnquiry #new added line

urlpatterns = [
    path('', create_user, name='create_user'),
    path('list/', list_users, name='list_user'),
    path('edit/<int:user_id>/', edit_user, name='update_user'),
    path('delete/<int:user_id>/', delete_user, name='delete_user'), 
    path ('saveenquiry/', saveEnquiry, name='saveenquiry') # Add this line #new added line
]
