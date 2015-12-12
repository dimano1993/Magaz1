from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, redirect
from django.template.context_processors import csrf
from basket.forms import OtlojitForm
from basket.models import Otlojit, notebook


def show_users(request):
    args = {}
    args.update(csrf(request))
    args["users"] = User.objects.all()
    args["username"] = auth.get_user(request).username
    users = User.objects.all()
    otl = Otlojit.objects.filter(sostoyanie="В обработке")
    b = []
    for us in users:
        for a in otl:
            if a.konkruser_id == us.id:
                b.append(a)
                break
    args["moiusers"] = b
    return render_to_response('modul/moiadmin.html', args)


def conkr_user(request, user_id):
    args = {}
    args.update(csrf(request))
    preuser = User.objects.get(id=user_id)
    user = preuser.username
    args["noytis"] = notebook.objects.all()
    args["user"] = user
    args["username"] = auth.get_user(request).username
    args["zakaz"] = Otlojit.objects.filter(user=user)
    return render_to_response('modul/conkruser.html', args)


def delete(request, zak_id):
    if request.POST:
        b = Otlojit.objects.get(id=zak_id)
        prepreuser = b.user
        preuser = User.objects.get(username=prepreuser)
        user = preuser.id
        b.sostoyanie = "Заказ удалён"
        b.save()
    return redirect('/show_users/%s' % user)


def ok(request, zak_id):
    if request.POST:
        b = Otlojit.objects.get(id=zak_id)
        prepreuser = b.user
        preuser = User.objects.get(username=prepreuser)
        user = preuser.id
        note = notebook.objects.get(id=b.konkrnote_id)
        note.amount = note.amount - b.zakaz
        b.sostoyanie = "Заказ обработан"
        note.save()
        b.save()
    return redirect('/show_users/%s' % user)


def doz(request, zak_id):
    if request.POST:
        b = Otlojit.objects.get(id=zak_id)
        prepreuser = b.user
        preuser = User.objects.get(username=prepreuser)
        user = preuser.id
        note = notebook.objects.get(id=b.konkrnote_id)
        note.amount = note.amount - (note.amount - b.zakaz)
        note.save()
    return redirect('/show_users/%s' % user)
