from django.urls import path, re_path, include
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('', views.index),
    re_path('^view/(?P<id>[0-9]+)', views.view),
    re_path('^search/', views.search, name='search'),
    re_path('^(?P<venue>[\w]+)/$', views.category),
]
