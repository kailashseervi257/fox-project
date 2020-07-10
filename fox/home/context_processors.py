from blog.models import Blog
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import datetime
from itertools import chain
def recentBlogs(request):
    resultQuerySet = Blog.objects.order_by('pub_date').filter(status=1).reverse()[:3]
    return {'recBlogs':resultQuerySet}