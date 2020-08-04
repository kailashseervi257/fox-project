from django.shortcuts import render, redirect, get_object_or_404
from .models import Enquiry, Contact_request, Subscribers
import re
from django.utils.timezone import datetime
from blog.models import Blog
from .forms import Engineering_Form, Medical_Form, Aviation_Form, Architecture_Form, PGMedical_Form, LawManagementCommerce_Form


homeForm = {
            'engg_form': Engineering_Form(),
            'med_form': Medical_Form(),
            'aviation_form': Aviation_Form(),
            'arch_form': Architecture_Form(),
            'PGmed_form': PGMedical_Form(),
            'LMC_form':LawManagementCommerce_Form(),
        }



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
        return render(request, 'home/contact.html')


def new_enquiry(request):
    homeForm = {
            'engg_form': Engineering_Form(),
            'med_form': Medical_Form(),
            'aviation_form': Aviation_Form(),
            'arch_form': Architecture_Form(),
            'PGmed_form': PGMedical_Form(),
            'LMC_form':LawManagementCommerce_Form(),
        }
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
                homeForm['message']='Message successfully sent'
                return render(request, 'home/home.html',homeForm)
            else:
                homeForm['error']='Invalid phone number'
                return render(request,'home/home.html',homeForm)
        else:
            homeForm['error']='All fields required.'
            return render(request,'home/home.html',homeForm)
    else:
        homeForm = {
            'engg_form': Engineering_Form(),
            'med_form': Medical_Form(),
            'aviation_form': Aviation_Form(),
            'arch_form': Architecture_Form(),
            'PGmed_form': PGMedical_Form(),
            'LMC_form':LawManagementCommerce_Form(),
        }
        return render(request, 'home/home.html',homeForm)


def forms(request):
    homeForm = {
            'engg_form': Engineering_Form(),
            'med_form': Medical_Form(),
            'aviation_form': Aviation_Form(),
            'arch_form': Architecture_Form(),
            'PGmed_form': PGMedical_Form(),
            'LMC_form':LawManagementCommerce_Form(),
        }
    if request.method == 'POST':
        form = Engineering_Form(data=request.POST)
        Pattern = re.compile("^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$")
        if form.is_valid() and Pattern.match(request.POST['phone']) and len(request.POST['phone']) >= 10:
            form.created_on = datetime.now()
            new_form = form.save(commit=False)
            new_form.save()
            # homeForm['new_form']='Successfully submitted....'
            homeForm['message'] = 'Applied successfully !'
            return render(request, 'home/home.html',homeForm)
        if form.errors:
            homeForm['error'] = form.errors
            return render(request, 'home/home.html',homeForm)
    homeForm = {
            'engg_form': Engineering_Form(),
            'med_form': Medical_Form(),
            'aviation_form': Aviation_Form(),
            'arch_form': Architecture_Form(),
            'PGmed_form': PGMedical_Form(),
            'LMC_form':LawManagementCommerce_Form(),
        }
    return render(request, 'home/home.html',homeForm)
        
def subscribe(request):
    homeForm = {
            'engg_form': Engineering_Form(),
            'med_form': Medical_Form(),
            'aviation_form': Aviation_Form(),
            'arch_form': Architecture_Form(),
            'PGmed_form': PGMedical_Form(),
            'LMC_form':LawManagementCommerce_Form(),
        }
    if request.method == "POST":
        subs = Subscribers.objects.all()
        new_sub=None
        if request.POST['email']:
            if request.POST['email'] not in str(subs):
                formInfo = Subscribers()
                formInfo.email = request.POST['email']
                formInfo.created_on=datetime.now()
                new_sub = formInfo.email
                formInfo.save()
                homeForm['message']='Added to mail list'
                return render(request, 'home/home.html',homeForm)
            else:
                homeForm['message']='You have already subscribed!'
                return render(request, 'home/home.html', homeForm)
    homeForm = {
            'engg_form': Engineering_Form(),
            'med_form': Medical_Form(),
            'aviation_form': Aviation_Form(),
            'arch_form': Architecture_Form(),
            'PGmed_form': PGMedical_Form(),
            'LMC_form':LawManagementCommerce_Form(),
        }
    return render(request, 'home/home.html', homeForm)
    


def Medforms(request):
    homeForm = {
            'engg_form': Engineering_Form(),
            'med_form': Medical_Form(),
            'aviation_form': Aviation_Form(),
            'arch_form': Architecture_Form(),
            'PGmed_form': PGMedical_Form(),
            'LMC_form':LawManagementCommerce_Form(),
        }
    if request.method == 'POST':
        form = Medical_Form(data=request.POST)
        Pattern = re.compile("^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$")
        if form.is_valid() and Pattern.match(request.POST['phone']) and len(request.POST['phone']) >= 10:
            form.created_on = datetime.now()
            new_form = form.save(commit=False)
            new_form.save()
            # homeForm['new_form']='Successfully submitted....'
            homeForm['message'] = 'Applied successfully !'
            return render(request, 'home/home.html',homeForm)
        if form.errors:
            homeForm['error'] = form.errors
            return render(request, 'home/home.html',homeForm)
    homeForm = {
            'engg_form': Engineering_Form(),
            'med_form': Medical_Form(),
            'aviation_form': Aviation_Form(),
            'arch_form': Architecture_Form(),
            'PGmed_form': PGMedical_Form(),
            'LMC_form':LawManagementCommerce_Form(),
        }
    return render(request, 'home/home.html', homeForm)
    
def Aviationform(request):
    homeForm = {
            'engg_form': Engineering_Form(),
            'med_form': Medical_Form(),
            'aviation_form': Aviation_Form(),
            'arch_form': Architecture_Form(),
            'PGmed_form': PGMedical_Form(),
            'LMC_form':LawManagementCommerce_Form(),
        }
    if request.method == 'POST':
        form = Aviation_Form(data=request.POST)
        Pattern = re.compile("^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$")
        if form.is_valid() and Pattern.match(request.POST['phone']) and len(request.POST['phone']) >= 10:
            form.created_on = datetime.now()
            new_form = form.save(commit=False)
            new_form.save()
            # homeForm['new_form']='Successfully submitted....'
            homeForm['message'] = 'Applied successfully !'
            return render(request, 'home/home.html',homeForm)
        if form.errors:
            homeForm['error'] = form.errors
            return render(request, 'home/home.html',homeForm)
    homeForm = {
            'engg_form': Engineering_Form(),
            'med_form': Medical_Form(),
            'aviation_form': Aviation_Form(),
            'arch_form': Architecture_Form(),
            'PGmed_form': PGMedical_Form(),
            'LMC_form':LawManagementCommerce_Form(),
        }
    return render(request, 'home/home.html', homeForm)
    

def Architectureform(request):
    homeForm = {
            'engg_form': Engineering_Form(),
            'med_form': Medical_Form(),
            'aviation_form': Aviation_Form(),
            'arch_form': Architecture_Form(),
            'PGmed_form': PGMedical_Form(),
            'LMC_form':LawManagementCommerce_Form(),
        }
    if request.method == 'POST':
        form = Architecture_Form(data=request.POST)
        Pattern = re.compile("^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$")
        if form.is_valid() and Pattern.match(request.POST['phone']) and len(request.POST['phone']) >= 10:
            form.created_on = datetime.now()
            new_form = form.save(commit=False)
            new_form.save()
            # homeForm['new_form']='Successfully submitted....'
            homeForm['message'] = 'Applied successfully !'
            return render(request, 'home/home.html',homeForm)
        if form.errors:
            homeForm['error'] = form.errors
            return render(request, 'home/home.html',homeForm)
    homeForm = {
            'engg_form': Engineering_Form(),
            'med_form': Medical_Form(),
            'aviation_form': Aviation_Form(),
            'arch_form': Architecture_Form(),
            'PGmed_form': PGMedical_Form(),
            'LMC_form':LawManagementCommerce_Form(),
        }
    return render(request, 'home/home.html', homeForm)
    

def PGMedicalform(request):
    homeForm = {
            'engg_form': Engineering_Form(),
            'med_form': Medical_Form(),
            'aviation_form': Aviation_Form(),
            'arch_form': Architecture_Form(),
            'PGmed_form': PGMedical_Form(),
            'LMC_form':LawManagementCommerce_Form(),
        }
    if request.method == 'POST':
        form = PGMedical_Form(data=request.POST)
        Pattern = re.compile("^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$")
        if form.is_valid() and Pattern.match(request.POST['phone']) and len(request.POST['phone']) >= 10:
            form.created_on = datetime.now()
            new_form = form.save(commit=False)
            new_form.save()
            # homeForm['new_form']='Successfully submitted....'
            homeForm['message'] = 'Applied successfully !'
            return render(request, 'home/home.html',homeForm)
        if form.errors:
            homeForm['error'] = form.errors
            return render(request, 'home/home.html',homeForm)
    homeForm = {
            'engg_form': Engineering_Form(),
            'med_form': Medical_Form(),
            'aviation_form': Aviation_Form(),
            'arch_form': Architecture_Form(),
            'PGmed_form': PGMedical_Form(),
            'LMC_form':LawManagementCommerce_Form(),
        }
    return render(request, 'home/home.html', homeForm)
    

def LMCform(request):
    homeForm = {
            'engg_form': Engineering_Form(),
            'med_form': Medical_Form(),
            'aviation_form': Aviation_Form(),
            'arch_form': Architecture_Form(),
            'PGmed_form': PGMedical_Form(),
            'LMC_form':LawManagementCommerce_Form(),
        }
    if request.method == 'POST':
        form = LawManagementCommerce_Form(data=request.POST)
        Pattern = re.compile("^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$")
        if form.is_valid() and Pattern.match(request.POST['phone']) and len(request.POST['phone']) >= 10:
            form.created_on = datetime.now()
            new_form = form.save(commit=False)
            new_form.save()
            # homeForm['new_form']='Successfully submitted....'
            homeForm['message'] = 'Applied successfully !'
            return render(request, 'home/home.html',homeForm)
        if form.errors:
            homeForm['error'] = form.errors
            return render(request, 'home/home.html',homeForm)
    homeForm = {
            'engg_form': Engineering_Form(),
            'med_form': Medical_Form(),
            'aviation_form': Aviation_Form(),
            'arch_form': Architecture_Form(),
            'PGmed_form': PGMedical_Form(),
            'LMC_form':LawManagementCommerce_Form(),
        }
    return render(request, 'home/home.html', homeForm)
    