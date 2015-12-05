from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from basket.models import Otlojit


def show_users(request):
    args = {}
    args.update(csrf(request))
    args["users"] = User.objects.all()
    args["username"] = auth.get_user(request).username
    return render_to_response('modul/moiadmin.html', args)


def conkr_user(request, user_id):
    args = {}
    args.update(csrf(request))
    preuser = User.objects.get(id=user_id)
    user = preuser.username
    args["user"] = user
    #user = auth.get_user()
    args["username"] = auth.get_user(request).username
    args["zakaz"] = Otlojit.objects.filter(user=user)
    return render_to_response('modul/conkruser.html', args)