from django.shortcuts import render
from .models import *
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
