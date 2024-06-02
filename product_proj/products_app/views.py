""" Views for the Product Model """
from rest_framework import viewsets
from .serializers import ProductSerializers
from .models import Product
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    """ Product Viewset """
    queryset=Product.objects.all()
    serializer_class=ProductSerializers
