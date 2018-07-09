from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from accounts import views

urlpatterns = [
   url(r'^$', 	views.index, name="index"),
   url(r'^login/$', views.login, name='login'),
   url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
   url(r'^signup/$', views.signup, name='signup'),
   url(r'^profile/$', login_required(views.profile), name='profile'),
]