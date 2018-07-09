from django.conf.urls import url
from voice import views

urlpatterns = [
    url(r'^$', views.index, name='voice'),
    url(r'^voice_tiles/$', views.voice_tiles, name='voice_tiles'),
    url(r'^call/$', views.make_call, name='make_call'),
    url(r'^vhistory/$', views.vhistory, name='vhistory'),
    url(r'^kol/$', views.kol, name='kol'),
    url(r'^fwd/$', views.fwd, name='fwd'),
    url(r'^err/$', views.err, name='err'),
    #deletes
    url(r'^delete/(?P<id>\d+)/$',views.delete,name='delete'),
]