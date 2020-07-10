from django.db import models
from django.contrib.auth.models import User


class Enquiry(models.Model):
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
    message = models.TextField()
    requested_on=models.DateTimeField(auto_now=True)
    


    