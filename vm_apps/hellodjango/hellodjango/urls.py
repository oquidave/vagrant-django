from django.conf.urls import include, url
from django.contrib import admin
from accounts import urls as auth_urls
from sms import urls as sms_urls
from airtime import urls as airtime_urls
from voice import urls as voice_urls
from payments import urls as payments_urls
from dashboard import urls as dashboard_urls
from accounts import views as accounts_views

urlpatterns = [
    #url(r'^$',accounts_views.index, name="index"),
    url(r'^',include(auth_urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include(auth_urls)),
    url(r'^sms/', include(sms_urls)),
    url(r'^dashboard/', include(dashboard_urls)),
    url(r'^airtime/', include(airtime_urls)),
    url(r'^voice/', include(voice_urls)),
    url(r'^payments/', include(payments_urls)),
]
