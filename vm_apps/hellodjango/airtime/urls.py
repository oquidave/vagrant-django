from django.conf.urls import url
from airtime import views

urlpatterns = [
    url(r'^$', views.index, name='airtime'),
    url(r'^send/$', views.send_airtime, name='send_airtime'),
    url(r'^at/$',views.at, name="at"),
    url(r'^pay/$',views.pay,name="pay"),
    url(r'^xs/$',views.xs,name="xs"),
    url(r'^era/$',views.era,name="era"),
    url(r'^athistory/$',views.athistory,name="athistory"),
]