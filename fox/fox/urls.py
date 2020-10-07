from django.contrib import admin
from django.urls import path,include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from home import views
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from blog.models import Blog


info_dict = {
    'queryset': Blog.objects.all(),
}


urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('admin/', admin.site.urls),
    path('blog/',include('blog.urls')),
    path('staff/',include('staff.urls')),
    path('course/', include('course.urls')),
    path('', include('home.urls')),
    re_path(r'^search/', include(('search.urls', 'search'), namespace='search')),
    path('sitemap.xml', sitemap, # new
        {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6)}},
        name='django.contrib.sitemaps.views.sitemap'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns=urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)