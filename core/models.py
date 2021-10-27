from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    '''
    A model to store user information
    '''
    avatar = models.ImageField(null=True, blank=True, upload_to='users_avatars')
