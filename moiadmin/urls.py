from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'moiadmin.views.show_users', name='show_users'),
    url(r'^(?P<user_id>[0-9]+)$',
        'moiadmin.views.conkr_user', name='conkr_user'),
    url(r'^(?P<zak_id>[0-9]+)/del$', 'moiadmin.views.delete', name='delete'),
    url(r'^(?P<zak_id>[0-9]+)/ok$', 'moiadmin.views.ok', name='ok'),
    url(r'^(?P<zak_id>[0-9]+)/doz$', 'moiadmin.views.doz', name='doz'),
]
