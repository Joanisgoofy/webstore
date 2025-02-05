import string
import random
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=225, unique=True)

    def __str__(self):
        return self.name
    

class Brand(models.Model):
    id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=225, unique=True)
    image = models.ImageField(upload_to="brand_images")

    def __str__(self):
        return self.name
    
class ImageFiled(models.Model):
    image = models.ImageField(upload_to='product_images')



class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=225)
    description = models.TextField()
    display_image = models.ImageField(upload_to="product_display_images")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    # images = models.ManyToManyField(ImageFiled)  
    uploaded_at = models.DateTimeField(auto_now_add=True)  

    class Meta:
        ordering = ["uploaded_at"]

    def __str__(self):
        return self.name
    

class CartItem(models.Model):
    id = models.AutoField(primary_key=True)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    

    @property
    def cost(self):
        return self.Product.price * self.quantity
    
    def __str__(self):
        return f"{self.Product.name} x {self.quantity}"

    

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ForeignKey(CartItem, on_delete=models.CASCADE)
    


    @property
    def total_cost(self):
        return sum(item.cost for item in self.items.all())
    
    def __str__(self):
        return self.user.username
    


class Order(models.Model):
    class status(models.TextChoices):
        PROCESSING = 'processing'
        COMPLETED = 'completed'
        CANCELLED = 'cancelled'
    id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    code = models.CharField(max_length=50)

    def self(self, *args, **kwargs):
        if not self.code:
            self.code = self.generate_unique_code()
        super().save(*args, **kwargs)

    def generate_unique_code(self):
        while True:
            code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            if not Order.objects.filter(code=code).exists():
                return code
    


class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    refrence_id = models.CharField(max_length=12, unique=True)
    status = models.CharField(max_length=20, default="processing")
    time = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        if self.order:
            self.amount = self.order.cart.total_cost
            self.user = self.order.cart.user 
        super().save(*args, **kwargs)




