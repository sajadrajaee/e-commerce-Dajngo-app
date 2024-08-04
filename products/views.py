from django.shortcuts import render
from .models import *

def featured_products(request):
    queryset = FeaturedProducts.objects.all()
    return render(
        request, 'setapp/index.html', {'queryset':queryset}
    )