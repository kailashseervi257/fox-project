from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from . import views

urlpatterns = [
    path('form/',views.forms,name="forms"),
    path('', views.new_enquiry, name="home"),
    path('subscribe/', views.subscribe, name="subscribe"),
    path('Medicalform/', views.Medforms, name='Medicalform'),
    path('Aviationform/', views.Aviationform, name='Aviationform'),
    path('Architectureform/', views.Architectureform, name='Architectureform'),
    path('PGMedicalform/', views.PGMedicalform, name='PGMedicalform'),
    path('LMCform/', views.LMCform, name='LMCform'),
]