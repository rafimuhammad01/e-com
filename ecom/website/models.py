from django.db import models
from django.utils.timezone import now
from django.utils.crypto import get_random_string
import string

# Create your models here.

class Tag(models.Model) :
    name = models.CharField(max_length=50)
    popular = models.BooleanField(default=False)

    def __str__(self) :
        return self.name


class Address(models.Model) :
    jalan = models.CharField(max_length=50)
    kecamatan = models.CharField(max_length=50)
    kota = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)

    def __str__(self) :
        return str(self.jalan) + " - " + self.zipcode

class Review (models.Model) :
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    review = models.TextField(max_length=200)
    rate = models.IntegerField(null=True, blank=True, choices=[
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5) 
    ])
    
    def __str__(self) :
        return "review" + " "+"(" + str(self.rate) + ")"

class Product(models.Model) :
    name = models.CharField(max_length=50)
    price = models.FloatField(max_length=50, default=0)
    description = models.TextField(max_length=200)
    tags = models.ManyToManyField(Tag)
    rate = models.FloatField(blank=True, max_length=1, null=True)
    review = models.ManyToManyField(Review, blank=True)
    image = models.ImageField(default='image/default.png', upload_to='image')

    def __str__ (self) :
        return "{} ({})".format(self.name, self.price)

class Customer(models.Model):
    name = models.CharField(max_length=50) 
    username = models.CharField(max_length=50)
    addres = models.ForeignKey(Address, on_delete=models.CASCADE,null=True, blank=True)
    cart = models.ManyToManyField('ProductOrder', blank=True, null=True, related_name='customer_cart')
    wishlist = models.ManyToManyField(Product, blank=True, related_name='customer_wishlist') 
    email_verification = models.BooleanField(default=False)
    email_verification_key = models.CharField(max_length=32)
    
    def __str__(self) :
        return self.name


class ProductOrder(models.Model) :
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    price= models.FloatField(default=0)
    def __str__ (self) :
        return "{}, {}, ({})".format(self.product,self.qty, self.price)

    

class Order(models.Model) :
    order_id = models.CharField(max_length=50, primary_key=True, default=get_random_string(8, allowed_chars=string.ascii_uppercase + string.digits))
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ManyToManyField(ProductOrder) 
    totalPrice = models.FloatField(max_length=50)
    date = models.DateTimeField(default=now)
    status = models.CharField(max_length=64,default='waiting_for_payment', choices=[
        ('waiting_for_payment', 'Waiting for Payment'),
        ('verified', 'Verified'),
        ("on_shipping", 'On Shipping'),
        ("arrived", 'Arrived'),
        ('finish', 'Finish') 
    ])

    def __str__(self) :
        return self.order_id























