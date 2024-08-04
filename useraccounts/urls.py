from django.urls import path
from . import views

app_name="useraccounts"

urlpatterns = [
    path('login/', views.loginpage, name="login"),
]
