from django.shortcuts import render, get_object_or_404
from products.models import *
from .models import CartItems

def cart(request):
    items = CartItems.objects.all()
    return render(
        request, 'carts/addToCart.html', {"items":items}
    )
    
def add_to_cart(request, product_id):
    pass