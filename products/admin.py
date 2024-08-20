from django.contrib import admin
from .models import *

# class ColorOfProductInline(admin.TabularInline):
#     model = ColorOfProduct
#     extra = 1 # it helps to add more choices for product
    
class ColorInline(admin.TabularInline):
    model = Colors
    extra = 1
@admin.register(ModelOfDay) 
class ModelOfDayProduct(admin.ModelAdmin):
    inlines = [ColorInline]
     
admin.site.register(NewProducts)
admin.site.register(FeaturedProducts)
