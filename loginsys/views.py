# -*- coding: utf-8 -*-

from django.contrib import auth
from django.shortcuts import render, redirect, render_to_response
from django.template.context_processors import csrf
from Registration.models import notebook
from django.contrib.auth.forms import UserCreationForm


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "Пользователь не найден"
            return render_to_response('auth/login.html', args)
    else:
        return render_to_response('auth/login.html', args)


def logout(request):
    auth.logout(request)
    return redirect('/')


def registration(request):
    return render_to_response('auth/registration.html',
                              {'noytis': notebook.objects.all(), 'username': auth.get_user(request).username})


def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm(request.POST)
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser_form = auth.authenticate(username=newuser_form.cleaned_data['username'],
                                             password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser_form)
            return redirect('/')
        else:
            args['form'] = newuser_form
    return render_to_response('auth/register.html', args)