from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts', include('useraccounts.urls')),
    path('', include('setapp.urls')),
    path('products/', include('products.urls')),
    path('carts/', include('carts.urls')),
    path('blogs/', include('blogs.urls'))
]
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
