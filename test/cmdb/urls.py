from django.contrib import admin
from django.urls import path,re_path
from .views import *

urlpatterns = [
    re_path(r'idcs/(?P<pk>\d+)?/?$',IdcView.as_view()),
    re_path(r'get_idcs/?$',idcs),
    # re_path(r'api_idcs/(?P<pk>\d+)?/?$',APIIdcView.as_view()),
    # re_path(r'^user/(?P<pk>\d+)/(?P<pk1>\d+)/$',user)

]