from django.conf.urls import url

__author__ = 'Дмитрий'

urlpatterns = [
    url(r'^login/', 'loginsys.views.login'),
    url(r'^logout/', 'loginsys.views.logout'),
]
