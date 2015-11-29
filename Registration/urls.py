from django.conf.urls import url


__author__ = 'Дмитрий'

urlpatterns = [
    url(r'^registration/$', 'Registration.views.registration', name='registration'),
    url(r'^home/$', 'Registration.views.home', name='home'),
    url(r'^$', 'Registration.views.home', name='home'),
]
