from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.urls import reverse
import datetime


# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    confirm_password=models.CharField(max_length=100)

    def register(self):
        self.save()



class Category(models.Model):
    category_name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=200,blank=True)

    def save(self,*args,**kwargs):
        self.slug=slugify(self.category_name)
        super(Category,self).save(*args,**kwargs)

    def __str__(self):
        return self.category_name
    
class Quantityvariant(models.Model):
    variant_name=models.CharField(max_length=100)

    def __str__(self):
        return self.variant_name
    

class Colorvariant(models.Model):
    color_name=models.CharField(max_length=100)
    color_code=models.CharField(max_length=100)

    def __str__(self):
        return self.color_name
    

class Sizevariant(models.Model):
    size_name=models.CharField(max_length=100)

    def __str__(self):
        return self.size_name
    

class Product(models.Model):
    Category=models.ForeignKey(Category,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='media/')
    price=models.FloatField()
    description=models.TextField()
    stock=models.IntegerField(default=100)

    quantity_type=models.ForeignKey(Quantityvariant,blank=True,null=True,on_delete=models.PROTECT)
    color_type=models.ForeignKey(Colorvariant,blank=True,null=True,on_delete=models.PROTECT)
    size_type=models.ForeignKey(Sizevariant,blank=True,null=True,on_delete=models.PROTECT)

    def __str__(self):
        return self.product_name
    
class Productimage(models.Model):
    product=models.ForeignKey(Product,on_delete=models.PROTECT)
    image=models.ImageField(upload_to='media/')



class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    dob = models.DateField(null=True)
    city = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=50, null=True)
    contact = models.CharField(max_length=10, null=True)
    image = models.FileField(null=True)

    def __str__(self):
        return self.user.username
class Cart(models.Model):
    cart_id=models.CharField(max_length=250,blank=True)
    date_added=models.DateTimeField(auto_now=True)

    class Meta:
        db_table='Cart'
        ordering=['date_added']
    def __str__(self):
         return '{}'.format(self.cart_id)
class CartItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)
    class Meta:
        db_table='CartItem'
    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return '{}'.format(self.product)





class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Status(models.Model):
    name = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name



class Wish(models.Model):
    
    wishtitle = models.CharField(max_length=250,unique=True)
    wish = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)
    date = models.DateField(default=datetime.date.today)
    is_achieved = models.BooleanField(default=False, blank=True)
    image = models.ImageField(upload_to='images/')
    
   
    def __str__(self):
        return  self.wishtitle



