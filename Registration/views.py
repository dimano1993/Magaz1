from django.shortcuts import render, render_to_response
from Registration.models import notebook
from django.contrib import auth


# не использую
def registration2(request):
    return render(request, 'site/registration.html')


def registration(request):
    return render_to_response('site/registration.html', {'noytis': notebook.objects.all(), 'username': auth.get_user(request).username})


# не использую
def login2(request):
    return render(request, 'site/login.html')


def login(request):
    return render_to_response('site/login.html', {'noytis': notebook.objects.all(), 'username': auth.get_user(request).username})


# не использую
def home2(request):
    noytis = notebook.objects.all()
    context = {
        'noytis': noytis
    }
    return render(request, 'site/home.html', context)


def home(request):
    return render_to_response('site/home.html', {'noytis': notebook.objects.all(), 'username': auth.get_user(request).username})