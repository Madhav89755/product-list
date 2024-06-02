""" Filter classes """
from django_filters import rest_framework as filters
from .models import Product

class ProductFilter(filters.FilterSet):
    """ Custom Filter Class for Product Model """
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    name = filters.CharFilter(field_name="name", lookup_expr='icontains')
    category = filters.CharFilter(field_name="category", lookup_expr='icontains')

    class Meta:
        """ Meta Class """
        model = Product
        fields = ["name",
                  "category",
                  "currency"]
