from django.conf.urls import url
from sms import views

urlpatterns = [
    url(r'^$', views.index, name='sms'),
    url(r'^send/$', views.send_sms, name='send_sms'),
    url(r'^sacess/$', views.sacess, name='sacess'),
    url(r'^sms_schedule/$', views.sms_schedule, name='sms_schedule'),
    url(r'^smshistory/$',views.smshistory,name='smshistory'),
    url(r'^bulks/$',views.bulks,name='bulks'),
    url(r'^delete/(?P<id>\d+)/$',views.delete,name='delete'),
    ]