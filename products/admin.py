from django.contrib import admin
from .models import *

class ColorInline(admin.TabularInline):
    model = Colors
    extra = 1
@admin.register(Products) 
class ProductsAdmin(admin.ModelAdmin):
    list_display = [
        "category",
        "name_of_product",
        "price",
        "description",
    ]
    list_filter = ["name_of_product",]
    ordering = ("category",)
    inlines = [ColorInline]
    
admin.site.register(ProductCategory)