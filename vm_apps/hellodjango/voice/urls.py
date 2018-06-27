from django.conf.urls import url
from voice import views

urlpatterns = [
    url(r'^$', views.index, name='voice'),
    url(r'^call/$', views.make_call, name='make_call'),
    url(r'^vhistory/$', views.vhistory, name='vhistory'),
<<<<<<< Updated upstream
    url(r'^dial/$', views.dial, name='dial'),
    url(r'^fwd/$', views.fwd, name='fwd'),
    url(r'^err/$', views.err, name='err'),
=======
    url(r'^fwd/$', views.fwd, name='fwd'),
>>>>>>> Stashed changes
    url(r'^delete/(?P<id>\d+)/$',views.delete,name='delete'),
]