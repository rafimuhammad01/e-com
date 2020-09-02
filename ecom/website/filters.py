import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet) :

    class Meta:
        model = Product
        fields = {
            'price' : ['lt', 'gt'],
            'review__rate' : ['iexact']
        }
    
class ProductSearch(django_filters.FilterSet) :

    class Meta:
        model = Product
        fields = {
            'name' : ['icontains'],
        }