from django.conf.urls import url
from airtime import views

urlpatterns = [
    url(r'^$', views.index, name='airtime'),
    url(r'^buyhistory/$', views.buyhistory, name='buyhistory'),
    url(r'^at/$',views.at, name="at"),
    url(r'^pay/$',views.pay,name="pay"),
    url(r'^xs/$',views.xs,name="xs"),
    url(r'^era/$',views.era,name="era"),
    url(r'^athistory/$',views.athistory,name="athistory"),
    url(r'^delit/(?P<id>\d+)/$',views.delit,name='delit'),
    url(r'^delete/(?P<id>\d+)/$',views.delete,name='delete'),
    url(r'^buy/$',views.buy, name="buy"),
    url(r'^buy1/$',views.buy1, name="buy1"),
    url(r'^history/$',views.history, name="history"),
]

