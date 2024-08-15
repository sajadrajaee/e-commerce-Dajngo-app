from django.shortcuts import render
from .models import *
from django.db.models import Q
from blogs.models import BlogPost

def index(request):
    featured_products = FeaturedProducts.objects.all()
    new_products = NewProducts.objects.all()
    latest_posts = BlogPost.objects.all().order_by('-created_at')[:3]
    return render(
        request, 
        'products/index.html', 
        {
            'items' : featured_products, 
            'new_items' : new_products,
            'latest_posts' : latest_posts
        }
    )
    
def search_product(request):
    query = request.GET['query']
    newproducts = NewProducts.objects.filter(Q(product_name__icontains=query))
    featuredproducts = FeaturedProducts.objects.filter(Q(name_of_product__icontains=query))
    context = {"products":newproducts or featuredproducts}
    return render(request, 'products/search_products.html', context)

