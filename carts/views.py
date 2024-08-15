from django.shortcuts import render, get_object_or_404
from products.models import *

def cart(request):
    return render(
        request, 'carts/addToCart.html', {}
    )
    
def add_to_cart(request, product_id):
    product = get_object_or_404(NewProducts, id=product_id)
    