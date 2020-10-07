from django.contrib.sitemaps import Sitemap
from blog.models import Blog
from django.shortcuts import reverse
class StaticViewSitemap(Sitemap):
    def items(self):
        return ['about','contact',]
    def location(self, item):
        return reverse(item)

class BlogSitemap(Sitemap):
    def items(self):
        return Blog.objects.all()