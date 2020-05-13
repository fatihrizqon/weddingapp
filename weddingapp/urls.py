from django.contrib import admin
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('packages/', include('packages.urls')),
    path('pricing/', include('pricing.urls')),
    path('portfolios/', include('portfolios.urls')),
    path('contact/', include('contact.urls')),
]
