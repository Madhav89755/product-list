""" Product App models """
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Product(models.Model):
    """ This model is for saving the details regarding Products """
    name=models.CharField(_("Product Name"),
                          db_column="product_name",
                          max_length=250,
                          db_index=True)
    category=models.CharField(_("Category"),
                              db_column="product_category",
                              max_length=250,
                              db_index=True)
    price=models.FloatField(_("Price"),
                            db_column="product_price")
    currency=models.CharField(_("Currency"),
                              db_column="price_currency",
                              default="INR",
                              max_length=10)
    created_at = models.DateTimeField(auto_now_add=True,
                                      db_column="creation_date_time")
    updated_at = models.DateTimeField(auto_now=True,
                                      db_column="updation_date_time")

    def __str__(self):
        return self.name.title()

    class Meta:
        """ Meta class """
        ordering=['-created_at']
        verbose_name=_("Product")
        verbose_name_plural=_("Products")
