from django.conf.urls import url

__author__ = 'Дмитрий'

urlpatterns = [
    url(r'^register/', 'loginsys.views.register', name='registration'),
    url(r'^login/', 'loginsys.views.login'),
    url(r'^logout/', 'loginsys.views.logout'),
]
