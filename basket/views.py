from django.contrib import auth
from django.shortcuts import render_to_response
from basket.models import notebook
from .forms import OtlojitForm
from django.core.context_processors import csrf


def bask(request):
    otlojit_form = OtlojitForm
    #args = {}
    #args.update(csrf(request))
    #args["noytis"] = 'noytis': notebook.objects.all()
    #args["username"] = 'username': auth.get_user(request).username
    #args["3"] = otlojit_form
    return render_to_response(('cart/basket.html', otlojit_form), {'username': auth.get_user(request).username, 'noytis': notebook.objects.all()})
