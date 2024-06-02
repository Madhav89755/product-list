""" Views for the Product Model """
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter
from .serializers import ProductSerializers
from .models import Product
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    """ Product Viewset """
    queryset=Product.objects.all()
    serializer_class=ProductSerializers
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter
