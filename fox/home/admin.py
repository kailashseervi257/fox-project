from django.contrib import admin
from .models import Enquiry, Contact_request, Subscribers
from blog.models import Blog

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'applied_for', 'post_date')
    search_fields = ['full_name','applied_for', 'message']

@admin.register(Contact_request)
class contactAdmin(admin.ModelAdmin):
    list_display = ('name',  'email', 'requested_on')
    list_filter=('requested_on',)
    search_fields = ['name', 'message']





@admin.register(Subscribers)
class SubscribersAdmin(admin.ModelAdmin):
    list_display=('email',)
