from django.urls import path, re_path
from django.contrib import admin
from .views import (searchposts)

urlpatterns=[
    re_path(r'^$', searchposts, name='searchposts'),

]