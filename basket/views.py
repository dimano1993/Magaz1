from itertools import count
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, redirect, get_object_or_404
from basket.models import notebook, Otlojit
from .forms import OtlojitForm
from django.core.context_processors import csrf


def bask(request):
    otlojit_form = OtlojitForm
    args = {}
    args.update(csrf(request))
    args["noytis"] = notebook.objects.all()
    args["username"] = auth.get_user(request).username
    args["otlo"] = otlojit_form
    return render_to_response('cart/basket.html', args)


def show_note(request, note_id):
    otlojit_form = OtlojitForm
    args = {}
    args.update(csrf(request))
    note = get_object_or_404(notebook, id=note_id)

    #yslovie = Otlojit.objects.get()
    #if yslovie > 0:


    args["noytis"] = notebook.objects.all()
    args["username"] = auth.get_user(request).username
    args["otlo"] = otlojit_form
    args["notebook"] = note
    return render_to_response('cart/note.html', args)


def addotlojit(request, note_id):
    if request.POST:
        form = OtlojitForm(request.POST)
        args = {}
        args.update(csrf(request))
        user = auth.get_user(request)
        konkr2 = Otlojit.objects.all()
        konkr3 = konkr2.order_by('-id')
        #konkr = Otlojit.objects.filter(user=user).order_by('-id')
        if form.is_valid():
            #if konkr.zakaz > 0:
                #args['error'] = "Вы заказали меньше одного ноутбука"
                #return render_to_response('cart/note.html', args)
            #else:
                comment = form.save(commit=False)
                comment.konkrnote = notebook.objects.get(id=note_id)
                comment.konkruser = auth.get_user(request)
                comment.user = auth.get_user(request)
                form.save()
    return redirect('/basket/note/%s' % note_id)


def delotlojit(request, zak_id):
    if request.POST:
        b = Otlojit.objects.get(id=zak_id)
        b.delete()
    return redirect('/basket/zakaz')


def zakaz(request):
    args = {}
    args.update(csrf(request))
    user = auth.get_user(request)
    args["username"] = auth.get_user(request).username
    args["zakaz"] = Otlojit.objects.filter(user=user)
    return render_to_response('cart/zakaz.html', args)