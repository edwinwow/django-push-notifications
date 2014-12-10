from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required
from .api import gcm_list, apns_list, gcm_detail, apns_detail


urlpatterns = patterns("",
    # GCM API notifications
    url(r'^api/devices/gcm/$', gcm_list, name='api_devices_gcm_list'),
    url(r'^api/devices/gcm/(?P<registration_id>[\w-]+)/$',gcm_detail,name='api_devices_gcm_detail'),
    # APNS notifications
    url(r'^api/devices/apns/$',apns_list,name='api_devices_apns_list'),
    url(r'^api/devices/apns/(?P<registration_id>[\w-]+)/$', apns_detail,name='api_devices_apns_detail'),




)

