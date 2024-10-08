# Generated by Django 5.0.7 on 2024-08-18 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='cover_page_pic',
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='author',
            field=models.CharField(max_length=180, verbose_name='نویسنده'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=models.TextField(verbose_name='محتوا'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='تاریخ ایجاد بلاگ'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/blogs/images', verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(max_length=255, verbose_name='عنوان'),
        ),
    ]
