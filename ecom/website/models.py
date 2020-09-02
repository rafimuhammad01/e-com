from django.db import models

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
    rate = models.IntegerField(null=True, blank=True, max_length = 1, choices=[
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
    rate = models.FloatField(blank=True, null=True, max_length=1)
    review = models.ManyToManyField(Review, null=True, blank=True)
    image = models.ImageField(default='image/default.png', upload_to='image')

    def __str__ (self) :
        return "{} ({})".format(self.name, self.price)

class Cart(models.Model) :
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Wishlist(models.Model) :
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Customer(models.Model):
    name = models.CharField(max_length=50) 
    username = models.CharField(max_length=50)
    addres = models.ForeignKey(Address, on_delete=models.CASCADE,null=True, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, blank=True,null=True)
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE, blank=True,null=True)
    email_verification = models.BooleanField(default=False)
    email_verification_key = models.CharField(max_length=32)
    
    def __str__(self) :
        return self.name

class Order(models.Model) :
    order_id = models.CharField(max_length=50, primary_key=True)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    totalPrice = models.FloatField(max_length=50)

    def __str__(self) :
        return self.order_id























