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
        return "%s by %s"%(self.name, self.user.username)


class Material(models.Model):
    """
    A model to store material information.
    """
    vendor = models.ForeignKey(Vendor,on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to='materials_images')
    price = models.DecimalField(decimal_places=2, max_digits=20, default=0)

    def __str__(self):
        return "%s by %s"%(self.name, self.vendor.name)
