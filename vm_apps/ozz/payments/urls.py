from django.conf.urls import url
from payments import views

urlpatterns = [
    url(r'^$', views.index, name='payments'),
    url(r'^bulk_pay/$', views.bulk_pay, name='bulk_pay'),
    url(r'^payment_tiles/$', views.payment_tiles, name='payment_tiles'),
    url(r'^bulk_pay/$', views.bulk_pay, name='bulk_pay'),
    url(r'^schedule_pay/$', views.schedule_pay, name='schedule_pay'),
    url(r'^pcsv_download/$',views.pcsv_download,name="pcsv_download"),    
    url(r'^phistory/$', views.phistory, name='phistory'),
    url(r'^bulkpayhist/$', views.bulkpayhist, name='bulkpayhist'),
    #deletes
    url(r'^del_item/(?P<id>\d+)/$',views.del_item,name='del_item'),
    url(r'^del_deposit/(?P<id>\d+)/$',views.del_deposit,name='del_deposit'),
    url(r'^del_hist/$',views.del_hist,name="del_hist"),
    url(r'^deposits_del/$',views.deposits_del,name="deposits_del"),
]