from .models import Subscribers
from django import forms

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields=('email',)