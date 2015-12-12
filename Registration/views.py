from django.shortcuts import render_to_response
from basket.models import notebook
from django.contrib import auth


def home(request):
    return render_to_response('site/home.html',
                              {'noytis': notebook.objects.all(),
                               'username': auth.get_user(request).username})
