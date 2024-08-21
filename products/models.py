from django.db import models

class ProductCategory(models.Model):
    class Meta:
        verbose_name = "کتگوری اجناس"
        verbose_name_plural = "کتگوری اجناس" 
    category = models.CharField(max_length=150, verbose_name="کتگوری")
    
    def __str__(self):
        return self.category
class Products(models.Model):
    class Meta:
        verbose_name = "اجناس"
        verbose_name_plural = "اجناس"
    category = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE, verbose_name="کتگوری"
    )
    name_of_product = models.CharField(max_length=150, verbose_name="اسم جنس")
    description = models.CharField(max_length=350, verbose_name="توضیحات")
    price = models.IntegerField(verbose_name="قیمت")
    image = models.ImageField(
        upload_to="static/products/images", null=False, blank=True, verbose_name="قیمت"
    )
    
    def __str__(self):
        return self.name_of_product
    
class Colors(models.Model):
    class Meta:
        verbose_name = "رنگ"
        verbose_name_plural = "رنگ ها"
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name="محصول")
    color = models.CharField(max_length=50,verbose_name="رنگ")
    
    def __str__(self):
        return self.color