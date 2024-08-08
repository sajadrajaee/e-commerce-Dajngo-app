# Generated by Django 5.0.7 on 2024-08-08 03:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='content',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
