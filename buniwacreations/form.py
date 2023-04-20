from django import forms
from . models import CustomerMessageQuote

class CustomerMessageQuoteForm(forms.ModelForm):
    class Meta:
        model = CustomerMessageQuote
        fields = [ 'name',
                  'email',
                  'phone',
                  'service',
                  'message', 
                   ]

