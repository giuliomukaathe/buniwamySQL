from django import forms
from . models import Subscribers

class SubscribersForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = [ 'first_name',
                  'second_name',
                  'country',
                  'region',
                  'email', 
                   ]

