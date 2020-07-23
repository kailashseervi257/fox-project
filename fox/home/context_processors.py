from blog.models import Blog
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import datetime
from itertools import chain
from .forms import SubscriptionForm
def recentBlogs(request):
    resultQuerySet = Blog.objects.order_by('pub_date').filter(status=1).reverse()[:3]
    return {'recBlogs': resultQuerySet}
    
# def subscribeForm(request):
#     new_sub=None
#     if request.method == 'POST':
#         subscribe_form = SubscriptionForm(data=request.POST)
#         if subscribe_form.is_valid():
#             new_sub.save()
#     else:
#         subscribe_form = SubscriptionForm()
#     return {'subscribe_form':subscribe_form}