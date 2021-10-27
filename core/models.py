from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    '''
    A model to store user information
    '''
    avatar = models.ImageField(null=True, blank=True, upload_to='users_avatars')


class Vendor(models.Model):
    """
    A model to store vendor information.
    """
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    avatar = models.ImageField(null=True, blank=True, upload_to='vendors_avatars')

    def __str__(self):
        return "%s-%s"%(self.name, self.user.username)
