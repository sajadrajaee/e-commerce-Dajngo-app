from django.db import models

# Create your models here.
class NewProducts(models.Model):
    class Meta:
        verbose_name = "اجناس جدید"
        verbose_name_plural = "اجناس جدید"
    
class FeaturedProducts(models.Model):
    class Meta:
        verbose_name = 'اجناس ویژه'
        verbose_name_plural = 'اجناس ویژه'
    name_of_product = models.CharField(max_length=150)
    price = models.IntegerField()
    
    def __str__(self):
        return self.name_of_product
    