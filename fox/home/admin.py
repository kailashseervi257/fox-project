from django.contrib import admin
from .models import Enquiry, Contact_request, Subscribers, Engineering_form
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

@admin.register(Engineering_form)
class EngineeringFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone','branch' ,'created_on')
    list_filter = ('created_on', 'branch')




@admin.register(Subscribers)
class SubscribersAdmin(admin.ModelAdmin):
    list_display=('email', 'created_on')
