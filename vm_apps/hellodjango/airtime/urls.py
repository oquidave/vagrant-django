from django.conf.urls import url
from airtime import views

urlpatterns = [
    url(r'^$', views.index, name='airtime'),
    url(r'^send/$', views.send_airtime, name='send_airtime'),
]