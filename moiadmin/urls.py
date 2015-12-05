from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'moiadmin.views.show_users', name='show_users'),
    url(r'^(?P<user_id>[0-9]+)$', 'moiadmin.views.conkr_user',  name='conkr_users'),

]