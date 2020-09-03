from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(Address)
admin.site.register(Tag)
