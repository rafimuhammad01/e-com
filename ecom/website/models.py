from django.db import models

# Create your models here.
class Review (models.Model) :
    review = models.TextField(max_length=200)
    rate = models.CharField(max_length = 1, choices=[
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5") 
    ])

class Tag(models.Model) :
    name = models.CharField(max_length=50)

    def __str__(self) :
        return self.name


class Product(models.Model) :
    name = models.CharField(max_length=50)
    price = models.FloatField(max_length=50)
    popular = models.BooleanField()
    tags = models.ManyToManyField(Tag)
    

    def __str__ (self) :
        return self.name


class Cart(models.Model) :
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self) :
        return "Cart by " + str(self.user)

class Wishlist(models.Model) :
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self) :
        return "Wishlist by " + str(self.user)

class Address(models.Model) :
    jalan = models.CharField(max_length=50)
    kecamatan = models.CharField(max_length=50)
    kota = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)

    def __str__(self) :
        return str(self.user) + " - " + self.zipcode

class Customer(models.Model):
    name = models.CharField(max_length=50) 
    addres = models.ForeignKey(Address, on_delete=models.CASCADE,null=True, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, blank=True,null=True)
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE, blank=True,null=True)
    
    def __str__(self) :
        return self.name

class Order(models.Model) :
    order_id = models.CharField(max_length=50, primary_key=True)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    totalPrice = models.FloatField(max_length=50)

    def __str__(self) :
        return self.order_id

















