from django.shortcuts import render, redirect
from .form import CustomerMessageQuoteForm
from django.contrib import messages




# Create your views here.
def index(request):
    Teams = Team.objects.all()
    return render(request, "index.html", {'Teams': Teams})


def CustomerMessageQuote(request):
        if request.method == 'POST':
            form = CustomerMessageQuoteForm(request.POST)
            if form.is_valid:
                  form.save()
                  messages.info(request, '📲Thank you for contacting us! We will reach you soon.')
                  return redirect ('contact')
        else:
              form = CustomerMessageQuoteForm  
        return render(request, 'index.html')

