from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path('featured_p/', views.featured_products, name="featured_p"),
]
