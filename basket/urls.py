from django.conf.urls import url


__author__ = 'Дмитрий'

urlpatterns = [
    url(r'^note/(?P<note_id>[0-9]+)/$', 'basket.views.show_note',  name='show_note'),
    url(r'^note/(?P<note_id>[0-9]+)/add', 'basket.views.addotlojit',  name='addotlojit'),
    url(r'^zakaz$', 'basket.views.zakaz',  name='zakaz'),
    url(r'^$', 'basket.views.bask',  name='basket'),
]
