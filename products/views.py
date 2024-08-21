from django.shortcuts import render
from .models import *
from django.db.models import Q
from blogs.models import BlogPost

def index(request):

    latest_posts = BlogPost.objects.all().order_by('-created_at')[:3] 
    return render(
        request, 
        'products/index.html', 
        {
            'latest_posts' : latest_posts,
        }
    )
    
def search_product(request):
    query = request.GET['query']
    products_search = Products.objects.filter(Q(__icontains=query))
    return render(
        request, 'products/search_products.html', {"products":products_search}
    )