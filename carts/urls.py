from django.urls import path
from .views import * 

app_name = 'carts'

urlpatterns = [
    path('cart/', cart, name="cart"),
]
