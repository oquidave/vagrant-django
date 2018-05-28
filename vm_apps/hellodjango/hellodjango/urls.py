from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from accounts import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'hellodjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^home/$', views.home, name='home'),
]
