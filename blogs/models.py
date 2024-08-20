from django.db import models
from django.utils.translation import gettext_lazy as _

class BlogPost(models.Model):
    class Meta:
        verbose_name = 'وبلاگ'
        verbose_name_plural = 'وبلاگ'
        
    title = models.CharField(max_length=255, verbose_name="عنوان")
    author = models.CharField(max_length=180, verbose_name="نویسنده")
    created_at = models.DateField(auto_now_add=True, verbose_name="تاریخ ایجاد بلاگ")
    content = models.TextField( verbose_name="محتوا")
    image = models.ImageField(
        upload_to='static/blogs/images',
        null=True,
        blank=True,
        verbose_name="تصویر",
    )
    
    def __str__(self):
        return self.title