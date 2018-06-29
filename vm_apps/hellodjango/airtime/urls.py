from django.conf.urls import url
from airtime import views

urlpatterns = [
    url(r'^$', views.index, name='airtime'),
    url(r'^ozz_history/$', views.ozz_history, name='ozz_history'),
    url(r'^at/$',views.at, name="at"),
    url(r'^pay/$',views.pay,name="pay"),
    url(r'^drop_table/$',views.drop_table,name="drop_table"),
    url(r'^bulkhist/$',views.bulkhist,name="bulkhist"),
    url(r'^at_subscribe/$',views.at_subscribe,name="at_subscribe"),
    url(r'^atbulk/$',views.atbulk,name="atbulk"),
    url(r'^mm_history/$',views.mm_history,name="mm_history"),
    url(r'^delit/(?P<id>\d+)/$',views.delit,name='delit'),
    url(r'^rm/(?P<id>\d+)/$',views.rm,name='rm'),
    url(r'^delete/(?P<id>\d+)/$',views.delete,name='delete'),
    url(r'^buy/$',views.buy, name="buy"),
    url(r'^at_buy/$',views.at_buy, name="at_buy"),
    url(r'^history/$',views.history, name="history"),
]

