from django.conf.urls import url
from payments import views

urlpatterns = [
    url(r'^$', views.index, name='payments'),
    url(r'^send/$', views.send, name='send_money'),
    url(r'^phistory/$', views.phistory, name='phistory')
]