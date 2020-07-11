from django.shortcuts import render, redirect, get_object_or_404
from .models import Enquiry, Contact_request
import re
from django.utils.timezone import datetime
from blog.models import Blog
def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')

def services(request):
    return render(request, 'home/services.html')

def contact(request):
    if request.method == 'POST':
        if request.POST['name'] and request.POST['email'] and request.POST['subject'] and request.POST['message']:
            contactReq = Contact_request()
            contactReq.name = request.POST['name']
            contactReq.email = request.POST['email']
            contactReq.subject = request.POST['subject']
            contactReq.message = request.POST['message']
            contactReq.save()
            return redirect('contact')
        else:
            return render(request,'home/contact.html',{'error': 'All fields required.'})
    else:
        return render(request,'home/contact.html')

def new_enquiry(request):
    if request.method == 'POST':
        if request.POST['fullName'] and request.POST['interestedIn'] and request.POST['phone'] and request.POST['appliedFor'] and request.POST['message']:
            Pattern=re.compile("(0/91)?[7-9][0-9]{9}")
            if Pattern.match(request.POST['phone']) and len(request.POST['phone']) >= 10:
                formInfo = Enquiry()
                formInfo.full_name = request.POST['fullName']
                formInfo.interested_in = request.POST['interestedIn']
                formInfo.ph = request.POST['phone']
                formInfo.applied_for = request.POST['appliedFor']
                formInfo.message = request.POST['message']
                formInfo.post_date=datetime.now()
                formInfo.save()
                return render(request, 'home/home.html',{'message':'Message successfully sent'})
            else:
                return render(request,'home/home.html',{'error':'Invalid phone number'})
        else:
            return render(request,'home/home.html',{'error':'All fields required.'})
    else:
        return render(request, 'home/home.html')
        