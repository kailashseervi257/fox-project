from django.urls import path, re_path, include
from . import views
from search.views import searchposts


urlpatterns = [
    path('froala_editor/',include('froala_editor.urls')),
    path('', views.blog,name='blog'),
    path('<slug:slug>/', views.detail, name='details'),
    re_path(r'^$', searchposts, name='searchposts'),
    path('<str:cat>',views.category,name='category')
]