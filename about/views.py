from django.shortcuts import render
# from .models import Team


# Create your views here.
def about(request):
    return render(request, 'about/about.html')

# def OurTeam(request):
#     Teams = Team.objects.all()
#     return render(request, 'about/about.htmll', {'Teams': Teams})