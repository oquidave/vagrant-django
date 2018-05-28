from django.conf.urls import include, url
from django.contrib import admin
from accounts import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'hellodjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', views.login, name='login'),
    url(r'^home/$', views.login, name='home'),
]
