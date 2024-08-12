from django.urls import path
from .views import *

app_name = 'useraccounts'
urlpatterns = [
    path('login/', login, name="login"),
]
