""" Serializer files """

from rest_framework import serializers
from .models import Product

class ProductSerializers(serializers.ModelSerializer):
    """ Product Serializer class """
    class Meta:
        """ Meta class """
        model=Product
        fields="__all__"
        read_only_fields=["created_at",
                          "updated_at"]
