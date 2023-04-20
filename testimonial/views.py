from django.shortcuts import render
from .models import Testimonial

# Create your views here.
def Testi(request):
    Testimonials = Testimonial.objects.all()
    return render(request, 'testimonial/testimonial.html', {'Testimonials': Testimonials})