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
        return self.name


class Material(models.Model):
    """
    A model to store material information.
    """
    vendor = models.ForeignKey(Vendor,on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to='materials_images')
    price = models.DecimalField(decimal_places=2, max_digits=20, default=0)

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    """
    A model to store order items information.
    """
    material = models.ForeignKey(Material,on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    added = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    @property
    def total(self):
        return self.material.price*self.quantity


    def __str__(self):
        return "%s %s @ R%s each"%(self.quantity, self.material.name, self.material.price)


class Order(models.Model):
    """
    A model to store order information.
    """
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, blank=True, null=True)
    items = models.ManyToManyField(OrderItem, blank=True)
    placed_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    placed_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    delivery_date = models.DateField(null=True,blank=True)
    comment = models.TextField(max_length=500, blank=True, null=True)
    notification_sent = models.BooleanField(default=False)

    @property
    def total(self):
        total = 0
        for i in self.items.all():
            total += i.total
        return total

    def __str__(self):
        return "Order #%s from %s"%(self.id, self.vendor)
