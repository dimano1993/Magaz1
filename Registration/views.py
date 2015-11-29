from django.shortcuts import render
from Registration.models import notebook


def registration(request):
    return render(request, 'site/registration.html')


def login(request):
    return render(request, 'site/login.html')


def home(request):
    noytis = notebook.objects.all()
    context = {
        'noytis': noytis
    }
    return render(request, 'site/home.html', context)