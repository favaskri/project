from django.db import models
from django.contrib.auth.models import User  

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=200,verbose_name='Product Name')
    price=models.DecimalField(max_digits=10,decimal_places=2, verbose_name='Product Price')
    image=models.ImageField(upload_to='products/',verbose_name='Product Image')
    details=models.TextField(verbose_name='Product Details')

    def __str__(self):
        return self.name
def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # One cart per user
    products = models.ManyToManyField(Product, blank=True)       # A cart can have multiple products
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.user.username}"


