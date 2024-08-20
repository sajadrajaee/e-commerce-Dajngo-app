from django.db import models
class NewProducts(models.Model):
    class Meta:
        verbose_name = "اجناس جدید"
        verbose_name_plural = "اجناس جدید"
    product_name = models.CharField(max_length=255, verbose_name="اسم جنس", default=None)
    price  = models.IntegerField(verbose_name="قیمت", default=None, null=False, blank=False)
    description = models.CharField(max_length=255, verbose_name="توضیحات")
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

class ModelOfDay(models.Model):
    class Meta:
        verbose_name = "جنس روز"
        verbose_name_plural = "اجناس روز"
    name = models.CharField(max_length=155, verbose_name="اسم جنس")
    description = models.CharField(max_length=350, verbose_name="توضیحات")
    date_posted = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد پست")
    price = models.IntegerField(verbose_name="قیمت", null=False, blank=False, default=None)    
    image = models.ImageField(upload_to="static/products/images", verbose_name="تصویر جنس")
    def __str__(self):
        return self.name
    
    # we must create a method to count the rating

class Colors(models.Model):
    class Meta:
        verbose_name = "رنگ"
        verbose_name_plural = "رنگ ها"
    product = models.ForeignKey(ModelOfDay, on_delete=models.CASCADE, verbose_name="محصول")
    color = models.CharField(max_length=50,verbose_name="رنگ")
    
    def __str__(self):
        return self.product
    
    
    
    