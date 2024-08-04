from django.urls import path
from . import models

app_name = "products"
urlpatterns = [
    path('featured_p/', models.FeaturedProducts, name="featuredP"),
]
