from django.shortcuts import render
from .models import BlogPost

# Create your views here.
def blogs(request):
    posts = BlogPost.objects.all()
    return render(request, 'blogs/posts.html', {'posts':posts})