from django.shortcuts import render
from .models import Education, Experience, Award

# Create your views here.
def home(request):
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    awards = Award.objects.all()
    return render(request, "core/home.html", {'educations': educations, 'experiences': experiences, 'awards': awards})

def blog(request):
    return render(request, "core/blog.html")