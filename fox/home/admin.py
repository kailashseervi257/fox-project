from django.contrib import admin
from .models import Enquiry, Contact_request, Subscribers, Engineering_form, Medical_form, PopupForm,Aviation_form, Architecture_form,PGMedical_form, LawManagementCommerce_form
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
    list_display = ('name', 'phone','branch' ,'created_on',)
    list_filter = ('created_on', 'branch',)




@admin.register(Subscribers)
class SubscribersAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_on',)
    
@admin.register(Medical_form)
class MedicalFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone','branch' ,'created_on',)
    list_filter = ('created_on', 'branch',)

@admin.register(Aviation_form)
class AviationFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone' ,'created_on',)
    list_filter = ('created_on',)

@admin.register(Architecture_form)
class ArchitectureFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone' ,'created_on',)
    list_filter = ('created_on',)

@admin.register(PGMedical_form)
class PGMedicalFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone' ,'created_on','neet_score')
    list_filter = ('created_on',)

@admin.register(LawManagementCommerce_form)
class LMCFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone' ,'created_on','Law_Management_or_Commerce')
    list_filter = ('created_on', 'Law_Management_or_Commerce',)
    
@admin.register(PopupForm)
class PopupFormAdmin(admin.ModelAdmin):
    list_display=('name','post_date')