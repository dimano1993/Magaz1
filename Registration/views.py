from django.shortcuts import render


def registration (request):
    return render(request, 'site/registration.html')


def login(request):
    return render(request, 'site/login.html')


def home(request):
    return render(request, 'site/home.html')