# users/apps.py

from django.apps import AppConfig

class UsersConfig(AppConfig):  # Class name should be UsersConfig
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'  # Ensure this is 'users', matching your app's directory name
