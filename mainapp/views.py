from django.shortcuts import render
from products.models import *

def index(request):
    featured_products = FeaturedProducts.objects.all()
    new_products = NewProducts.objects.all()
    return render(
        request, 
        'mainapp/index.html', 
        {
            'items' : featured_products, 'new_items' : new_products
        }
    )
