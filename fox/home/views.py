from django.db.models.fields import EmailField
from django.shortcuts import render, redirect, get_object_or_404
from .models import Enquiry, Contact_request, Subscribers, PopupForm, RankPredictor
import re
from django.utils.timezone import datetime
import pytz
from blog.models import Blog
from .forms import Engineering_Form, Medical_Form, Aviation_Form, Architecture_Form, PGMedical_Form, LawManagementCommerce_Form
from django.core.mail import send_mail
from django.core.mail import mail_admins
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib import messages



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

def counsellingInfo(request):
    return render(request, "home/feature/counsellingInfo.html")

def admissionsInfo(request):
    return render(request, "home/feature/admissionsInfo.html")

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
            messages.success(request, "Submitted")
            return redirect('contact')
        else:
            messages.error(request, 'All fields required.')
            return render(request,'home/contact.html')
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
        IST=pytz.timezone('Asia/Kolkata')
        if request.POST['fullName'] and request.POST['interestedIn'] and request.POST['phone'] and request.POST['appliedFor'] and request.POST['message']:
            Pattern=re.compile("(0/91)?[7-9][0-9]{9}")
            if Pattern.match(request.POST['phone']) and len(request.POST['phone']) >= 10:
                formInfo = Enquiry()
                formInfo.full_name = request.POST['fullName']
                formInfo.interested_in = request.POST['interestedIn']
                formInfo.ph = request.POST['phone']
                formInfo.applied_for = request.POST['appliedFor']
                formInfo.message = request.POST['message']
                formInfo.post_date = datetime.now(IST)
                formInfo.save()
                subject = 'New enquiry form'
                message = 'Name: '+formInfo.full_name+'\ninterested in '+formInfo.interested_in+'\nPhone number: '+formInfo.ph+'\nHas applied for '+formInfo.applied_for+'\nMessage: '+formInfo.message+'\nRequest on: '+str(datetime.now(IST))
                email_from = settings.EMAIL_HOST_USER
                recipient_list=settings.EMAIL_RECIPIENTS_LIST
                # mail_admins(subject,message, fail_silently=False,connection=None, html_message=None)
                send_mail( subject, message, email_from, recipient_list )
                messages.success(request, "'Message successfully sent")
                return render(request, 'home/home.html',homeForm)
            else:
                messages.error(request, "Invalid phone number")
                return render(request,'home/home.html',homeForm)
        else:
            messages.error(request, "All fields required.")
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
            messages.error(request, "Applied successfully !")
            return render(request, 'home/home.html',homeForm)
        if form.errors:
            messages.error(request, form.errors)
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
                messages.success(request, 'Added to mail list')
                return render(request, 'home/home.html',homeForm)
            else:
                messages.success(request, "You have already subscribed!")
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


def popupForm(request):
    if request.method == 'POST':
        IST=pytz.timezone('Asia/Kolkata')
        if request.POST['name'] and request.POST['ph'] and request.POST['courseType'] and request.POST['Entrance'] and request.POST['TwelfthPercentage'] and request.POST['admissionType']:
            Pattern=re.compile("(0/91)?[7-9][0-9]{9}")
            if Pattern.match(request.POST['ph']) and len(request.POST['ph']) >= 10:
                formInfo = PopupForm()
                formInfo.name = request.POST['name']
                formInfo.ph = request.POST['ph']
                formInfo.courseType = request.POST['courseType']
                formInfo.Entrance = request.POST['Entrance']
                formInfo.TwelfthPercentage = request.POST['TwelfthPercentage']
                formInfo.admissionType = request.POST['admissionType']
                formInfo.post_date = datetime.now(IST)
                formInfo.save()
                subject = 'New Popup enquiry form'
                Emessage = 'Name: '+formInfo.name+'\n '+'\nPhone number: '+formInfo.ph+'\nCourse Type'+formInfo.courseType+'\nEntrance: '+formInfo.Entrance+'\nTwelfthPercentage'+formInfo.TwelfthPercentage+'Admission Type'+'\nRequest on: '+str(datetime.now(IST))
                email_from = settings.EMAIL_HOST_USER
                recipient_list=settings.EMAIL_RECIPIENTS_LIST
                # mail_admins(subject,emessage, fail_silently=False,connection=None, html_message=None)
                send_mail( subject, Emessage, email_from, recipient_list )
                messages.success(request, "Message successfully sent")
                return render(request, 'home/home.html',homeForm)
            else:
                messages.error(request, "Invalid phone number")
                return render(request, 'home/home.html',homeForm)
        else:
            messages.error(request, "Invalid phone number")
            return render(request,'home/home.html',homeForm)

def RankPredictorForm(request):
    if request.method=="POST":
        Name = request.POST.get("name")
        Email = request.POST.get("email")
        Exam = request.POST.get("exam")
        Score = request.POST.get("score")
        if Name and Email and Exam and Score:
            form = RankPredictor()
            form.Name=Name
            form.Email=Email
            form.Exam=Exam
            form.Score=Score
            form.save()

            subject = 'New Rank predictor request'
            Emessage = 'Name: '+Name+'\n '+'Email: '+Email+"\nExam: "+Exam+"\nScore: "+Score
            email_from = settings.EMAIL_HOST_USER
            recipient_list=settings.EMAIL_RECIPIENTS_LIST
            send_mail( subject, Emessage, email_from, recipient_list )
            messages.success(request, "Please check you mail inbox")
        else:
            messages.error(request, "All fields are required")
    return redirect('home')