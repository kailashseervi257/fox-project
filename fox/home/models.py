from django.db import models
from django.contrib.auth.models import User
from django.db.models import base
from django.db.models.fields import CharField, related
from django.utils.timezone import datetime


JEE = 'JEE'
NEET = 'NEET'
NEET_PG = 'NEET-PG'
CET = 'CET'
COMED_K = 'COMED-K'
OTHER='Other'
APPLIEDFOR = [
    (JEE,'JEE'),
    (NEET ,'NEET'),
    (NEET_PG,'NEET-PG'),
    (CET,'CET'),
    (COMED_K,'COMED-K'),
    (OTHER,'Other'),
]


class Enquiry(models.Model):
    full_name = models.CharField(max_length=50)
    interested_in = models.CharField(max_length=255)
    ph = models.CharField(max_length=12)
    applied_for = models.CharField(max_length=10,choices=APPLIEDFOR, default=OTHER)
    post_date = models.DateTimeField(auto_now=True)
    message = models.TextField()

    def __str__(self):
        return self.full_name

class Contact_request(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField(default=None)
    requested_on=models.DateTimeField(auto_now=True)
    
class Subscribers(models.Model):
    email = models.EmailField(unique=True)
    created_on=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.email


class Engineering_form(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=50)
    TwelfthPercentage = models.CharField(max_length=10)
    applied_for=models.CharField(max_length=10,choices=APPLIEDFOR, default=OTHER)
    branch = models.CharField(max_length=1000)
    college = models.CharField(max_length=50)
    created_on=models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_on']
        
    def __str__(self):
        return 'By {} on {}'.format(self.name,self.created_on)

class Medical_form(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=50)
    TwelfthPercentage = models.CharField(max_length=10)
    applied_for=models.CharField(max_length=10,choices=APPLIEDFOR, default=OTHER)
    branch = models.CharField(max_length=1000)
    college = models.CharField(max_length=50)
    created_on=models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_on']
        
    def __str__(self):
        return 'By {} on {}'.format(self.name, self.created_on)
        
class Aviation_form(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=50)
    TwelfthPercentage = models.CharField(max_length=10)
    college = models.CharField(max_length=50)
    created_on=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-created_on']
    
    def __str__(self):
        return 'By {} on {}'.format(self.name, self.created_on)

class Architecture_form(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=50)
    applied_for_NATA=models.BooleanField(default=False)
    TwelfthPercentage = models.CharField(max_length=10)
    college = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-created_on']
    
    def __str__(self):
        return 'By {} on {}'.format(self.name, self.created_on)

class PGMedical_form(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=50)
    neet_score = models.CharField(max_length=10)
    branch = models.CharField(max_length=1000)
    college = models.CharField(max_length=50)
    created_on=models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_on']
        
    def __str__(self):
        return 'By {} on {}'.format(self.name, self.created_on)

class LawManagementCommerce_form(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=50)
    TwelfthPercentage = models.CharField(max_length=10)
    branch = models.CharField(max_length=1000)
    college = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now=True)
    anyEntrance = models.BooleanField(default=False)
    Law_Management_or_Commerce=models.CharField(max_length=15, default='NA')
    class Meta:
        ordering = ['-created_on']
        
    def __str__(self):
        return 'By {} on {}'.format(self.name, self.created_on)

Counselling = 'Counselling'
DirectAdmissions = 'Direct Admissions'
AdmissionType = [
    (Counselling , 'Counselling'),
    (DirectAdmissions , 'Direct Admissions'),
]

KCET2020 = 'K-CET 2020'
COMEDK2020 = 'COMED-K2020'
NEET2020 = 'NEET2020'
JEEMAINS = 'JEE Mains 2020'
JEEADVANCE = 'JEE Advance 2020'
OTHER = 'Other'
entrance = [
    (KCET2020 ,'K-CET 2020'),
    (COMEDK2020 , 'COMED-K2020'),
    (NEET2020 , 'NEET2020'),
    (JEEMAINS , 'JEE Mains 2020'),
    (JEEADVANCE , 'JEE Advance 2020'),
    (OTHER,'Other'),
]

BEBTECH = 'BE / B.Tech'
Degree = 'Degree'
Paramedical = 'Paramedical'
Medical = 'Medical'
Architecture = 'Architecture'
CourseType = [
    (BEBTECH ,'BE / B.Tech'),
    (Degree ,'Degree'),
    (Paramedical , 'Paramedical'),
    (Medical , 'Medical'),
    (Architecture,'Architecture'),
]

class PopupForm(models.Model):
    name = models.CharField(max_length=25)
    ph = models.CharField(max_length=12)
    courseType = models.CharField(max_length=15,choices=CourseType)
    Entrance = models.CharField(max_length=20,choices=entrance, default=OTHER)
    TwelfthPercentage = models.CharField(max_length=10)
    post_date = models.DateTimeField(auto_now=True)
    admissionType = models.CharField(max_length=20,choices=AdmissionType)

    def __str__(self):
        return self.name

class RankPredictor(models.Model):
    Name = models.CharField(max_length=50, blank=True, null=True)
    Email = models.CharField(max_length=50, blank=True, null=True)
    Exam = models.CharField(max_length=50, blank=True, null=True)
    Score = models.CharField(max_length=50, blank=True, null=True)
    Date = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.Email

class CareerAddmission(models.Model):
    Name = models.CharField(max_length=50)
    Phone = models.CharField(max_length=50)
    Qualification = models.CharField(max_length=50, blank=True, null=True)
    FormType = models.CharField(max_length=50, choices=[('Career','Career'), ('Addmission', 'Addmission')])
    Details = models.CharField(max_length=100, blank=True, null=True)
    Date = models.DateTimeField(auto_now=True)

    def __str___(self):
        return self.Name