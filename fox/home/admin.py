from django.contrib import admin
from .models import Enquiry, Contact_request
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'applied_for', 'post_date')
    search_fields = ['full_name', 'message']

class contactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'requested_on')
    search_fields = ['name', 'message']
admin.site.register(Enquiry, EnquiryAdmin)
admin.site.register(Contact_request, contactAdmin)