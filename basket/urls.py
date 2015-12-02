from django.conf.urls import url


__author__ = 'Дмитрий'

urlpatterns = [
    #url(r'^test', 'basket.views.addotlojit',  name='basket'),
    url(r'^note/(?P<note_id>[0-9]+)/$', 'basket.views.show_note',  name='show_note'),
    url(r'^$', 'basket.views.bask',  name='basket'),
]
