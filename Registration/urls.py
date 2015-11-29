from django.conf.urls import url

__author__ = 'Дмитрий'

urlpatterns = [
    url(r'^registration/$', 'Registration.views.registration', name='registration'),
    url(r'^login/$', 'Registration.views.login', name='login'),
    url(r'^home/$', 'Registration.views.home', name='home'),
]
