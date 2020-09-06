from django.contrib import admin

# Register your models here.
from .models import *


class CustomerAdmin(admin.ModelAdmin) :
    filter_horizontal = ('cart','wishlist')

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(Address)
admin.site.register(Tag)
admin.site.register(ProductOrder)
