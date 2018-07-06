from django.conf.urls import url
from sms import views

urlpatterns = [
    url(r'^$', views.index, name='sms'),
    url(r'^send/$', views.send_sms, name='send_sms'),
    url(r'^sms_schedule/$', views.sms_schedule, name='sms_schedule'),
    url(r'^sms_csv_download/$', views.sms_csv_download, name='sms_csv_download'),
    url(r'^smshistory/$',views.smshistory,name='smshistory'),
    url(r'^sms_tiles/$',views.sms_tiles,name='sms_tiles'),    
    url(r'^bulks/$',views.bulks,name='bulks'),
    #deletes
    url(r'^delete/(?P<id>\d+)/$',views.delete,name='delete'),
    url(r'^smshist_delete/$',views.smshist_delete,name='smshist_delete'),
    ]