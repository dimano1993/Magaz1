from django.contrib import auth
from django.shortcuts import render, render_to_response
from basket.models import notebook


def bask(request):
    return render_to_response('cart/basket.html', {'noytis': notebook.objects.all(), 'username': auth.get_user(request).username})
