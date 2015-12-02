from django.contrib import auth
from django.shortcuts import render_to_response, redirect, get_object_or_404
from basket.models import notebook
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
    args["noytis"] = notebook.objects.all()
    args["username"] = auth.get_user(request).username
    args["otlo"] = otlojit_form
    args["notebook"] = note
    return render_to_response('cart/note.html', args)


#def addotlojit(request, noyt_id)
#    if request.POST:
#        form = OtlojitForm(request.POST)
#        if form.is_valid():
#            comment = form.save(commit=False)
#            comment.konkrnote = notebook.objects.get(id=noyt_id)
#            form.save()
#    return redirect('cart/basket.html')
