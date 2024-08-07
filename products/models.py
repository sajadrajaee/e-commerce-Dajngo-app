from django.db import models

# Create your models here.
class NewProducts(models.Model):
    class Meta:
        verbose_name = "اجناس جدید"
        verbose_name_plural = "اجناس جدید"
    product_name = models.CharField(max_length=255, verbose_name="اسم جنس", default=None)
    price  = models.IntegerField(verbose_name="قیمت", default=None, null=False, blank=False)
    image = models.ImageField(
        upload_to="static/products/images", verbose_name="تصویر", null=False, blank=False
    )
    
    def __str__(self):
        return self.product_name
class FeaturedProducts(models.Model):
    class Meta:
        verbose_name = 'اجناس ویژه'
        verbose_name_plural = 'اجناس ویژه'
    name_of_product = models.CharField(max_length=150, verbose_name="اسم جنس")
    # rating = models.IntegerField()
    price = models.IntegerField(verbose_name="قیمت")
    image = models.ImageField(upload_to="static/products/images", verbose_name="تصویر")
    def __str__(self):
        return self.name_of_product    