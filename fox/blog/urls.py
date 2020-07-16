from django.urls import path, re_path
from . import views
from search.views import searchposts
urlpatterns = [
    path('', views.blog,name='blog'),
    path('<slug:slug>/', views.detail, name='details'),
    re_path(r'^$', searchposts, name='searchposts'),
    path('<str:cat>',views.category,name='category')
]