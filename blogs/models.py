from django.db import models

class BlogPost(models.Model):
    class Meta:
        verbose_name = 'وبلاگ'
        verbose_name_plural = 'وبلاگ'
        
    cover_page_pic = models.ImageField(upload_to='static/blogs/images')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=180)
    created_at = models.TextField()
    image = models.ImageField(
        upload_to='static/blogs/images',
        null=True,
        blank=True
    )
    
    def __str__(self):
        return self.title