""" Admin Configurations for the models """
from django.contrib import admin
from .models import Product

# Register your models here.
@admin.register(Product)
class ProductAdminClass(admin.ModelAdmin):
    """ Model Admin configurations for Product Model """
    list_display=["id",
                  "name",
                  "category",
                  "price",
                  "currency",
                  "created_at"]
    list_filter=["category",
                 "currency"]
    search_fields=["id",
                   "name"]
    sortable_by=["id",
                 "price"]
