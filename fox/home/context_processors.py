from blog.models import Blog, HeaderBlogs
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import datetime
from itertools import chain
from .forms import SubscriptionForm
def recentBlogs(request):
    resultQuerySet = Blog.objects.order_by('pub_date').filter(status=1).reverse()[:3]
    return {'recBlogs': resultQuerySet}

def recentBlogsFooter(request):
    recentBlogFoot = Blog.objects.order_by('pub_date').filter(status=1).reverse()[:2]
    return {'recentBlogFoot': recentBlogFoot}


def homeHeaderBlogs(request):
    headBlog = HeaderBlogs.objects.all()[:4]
    g=[]
    for i in headBlog:
        b1 = get_object_or_404(Blog, title=i)
        g.append(b1.title)
    headBlogs = Blog.objects.filter(title__in=g)
    return {'headBlogs':headBlogs}


def show_popup_once_processor(request):
    show_popup = False
    if not request.session.get('popup_seen', False):
        request.session['popup_seen'] = True
        show_popup = True
    return { "show_popup": show_popup }
# def subscribeForm(request):
#     new_sub=None
#     if request.method == 'POST':
#         subscribe_form = SubscriptionForm(data=request.POST)
#         if subscribe_form.is_valid():
#             new_sub.save()
#     else:
#         subscribe_form = SubscriptionForm()
#     return {'subscribe_form':subscribe_form}
