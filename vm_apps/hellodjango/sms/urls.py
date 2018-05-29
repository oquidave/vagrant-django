from django.conf.urls import url
from sms import views

urlpatterns = [
    url(r'^$', views.index, name='sms'),
    url(r'^send/$', views.send_sms, name='send_sms'),
]