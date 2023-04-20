from django.shortcuts import render, redirect
from .form import SubscribersForm
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import send_mail
from .models import Subscribers
from django_pandas.io import read_frame
from django.template.loader import get_template


# Create your views here
def baseletter(request):
    emails = Subscribers.objects.all()
    df = read_frame(emails, fieldnames=['email'])
    mail_list = df['email'].values.tolist()
    print(mail_list)
    if request.method == 'POST':
        form = SubscribersForm(request.POST)
        if form.is_valid():
            form.save()
            title = 'Buniwa Creations'
            message = 'At Buniwa Creations, we are determined to help you grow. Keep following us on our Social Media Pages! If you would like to unsubscibe from our newsletter, please reply this email with a "UNSUBSCRIBE ME" message. Thank you'
            send_mail(
                    title,
                    message,
                    '',
                    mail_list,
                    fail_silently=False,)
            messages.info(request, "Congratulations🎈. We've Added You To Our Emailing List. Check Your Email To Confirm.")
            return redirect('/')
    else:
        form = SubscribersForm()
    context = {
        'form': form,
    }
    return render(request, 'letter/letterindex.html', context)




