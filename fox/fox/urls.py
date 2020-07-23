from django.contrib import admin
from django.urls import path,include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from home import views
urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('admin/', admin.site.urls),
    path('blog/',include('blog.urls')),
    path('staff/',include('staff.urls')),
    path('course/', include('course.urls')),
    path('', include('home.urls')),
    re_path(r'^search/',include(('search.urls', 'search'), namespace='search')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns=urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
