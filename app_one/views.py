from django.shortcuts import render
from .models import CV, Galery


def index(request):
    cv = CV.objects.all()
    galery = Galery.objects.all()
    return render(request, 'app_one/index.html', {'title': 'Home Page', 'cv': cv, 'galery': galery})

def about(request):
    return render(request, 'app_one/about.html')