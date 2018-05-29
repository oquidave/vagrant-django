from django.conf.urls import url
from voice import views

urlpatterns = [
    url(r'^$', views.index, name='voice'),
    url(r'^call/$', views.make_call, name='make_call'),
]