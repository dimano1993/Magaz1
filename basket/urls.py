from django.conf.urls import url


__author__ = 'Дмитрий'

urlpatterns = [
    url(r'^$', 'basket.views.bask',  name='basket'),
]
