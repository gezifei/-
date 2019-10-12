from django.contrib import admin
from django.urls import path,re_path
from .views import *

urlpatterns = [
    re_path(r'idcs/(?P<pk>\d+)?/?$',IdcView.as_view()),
    re_path(r'racks/(?P<pk>\d+)?/?$', RackView.as_view()),
]