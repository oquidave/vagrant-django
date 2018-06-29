from django.conf.urls import url
from payments import views

urlpatterns = [
    url(r'^$', views.index, name='payments'),
    url(r'^bulk_pay/$', views.bulk_pay, name='bulk_pay'),
    url(r'^phistory/$', views.phistory, name='phistory')
]