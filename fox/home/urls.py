from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from . import views

urlpatterns = [
    path('form/',views.forms,name="forms"),
    path('', views.new_enquiry, name="home"),
    path('subscribe/',views.subscribe,name="subscribe"),
]