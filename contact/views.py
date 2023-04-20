from django.shortcuts import render, redirect
from .models import CustomerMessage
from django.http import HttpResponse
from .form import CustomerMessageForm
from django.contrib import messages


# Create your views here.
def contact(request):
        if request.method == 'POST':
            form = CustomerMessageForm(request.POST)
            if form.is_valid:
                  form.save()
                  messages.info(request, '📲Thank you for contacting us! We will reach you soon.')
                  return redirect ('contact')
        else:
              form = CustomerMessageForm

        
        return render(request, 'contact/contact.html')