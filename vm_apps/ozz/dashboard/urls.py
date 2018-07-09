from django.conf.urls import url
from dashboard import views

urlpatterns = [
    url(r'^$', views.index, name='dashboard'),
    url(r'^sms/$', views.sms, name='sms'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^airtime/$', views.airtime, name='airtime_page'),
    url(r'^voice/$', views.voice, name='voice'),
]