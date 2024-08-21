from django.db import models
from accounts.models import CustomUser
from products.models import *

class CartItems(models.Model):
    class Meta:
        verbose_name = "کارت"
        verbose_name_plural = "کارت"
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name="محصول")
    quantity = models.PositiveIntegerField(verbose_name="مقدار")
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="مشتری")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ اضافه شده به سبد خرید")
    
    def __str__(self):  
        return self.product
    