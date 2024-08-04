from django.urls import path
from . import views
app_name = "setapp"
urlpatterns = [
    path('', views.index, name="index"),
]