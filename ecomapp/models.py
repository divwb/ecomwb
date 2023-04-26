from django.contrib.auth.models import User
from django.db import models

# Create your models here.

CATEGORY_CHOICES=(
    ('CR','Curd'),
    ('ML','Milk'),
    ('PN','Paneer'),
    ('Ic','Icecream'),
    ('GH','Ghee'),
    ('CZ','Cheese'),
)
class Product(models.Model):
    objects = None
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    discounted_price=models.FloatField()
    desc=models.TextField()
    composition=models.TextField(default='')
    prodapp=models.TextField(default='')
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    image=models.ImageField(upload_to='product')

    def __str__(self):
        return self.name

class Customer(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=100)
    mobile=models.IntegerField(default=0)
    zipcode=models.IntegerField()
    state=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

class OrderPlaced(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    ordered_date=models.DateTimeField(auto_now_add=True)
    def total_cost(self):
        return self.quantity * self.product.discounted_price







