from django.conf.urls import url
from appmobile import views
from .api import MobileDeviceList, MobileDeviceDetail

"""
urlpatterns = [
    url(r'^$', views.index, name='appmobile'),
    url(r'^services/$', views.services, name='app_sevices'),
    url(r'^view_message/(?P<message_id>\w+)/$', views.view_message, name='view_message'),

]
"""
urlpatterns = [
    # Usando servicios de REST
    url(r'^$', MobileDeviceList.as_view(), name='messages'),
    #url(r'^message/(?P<message_id>\w+)/$', MobileDeviceDetail.as_view(), name='view_message'),

    # por templates de django
    url(r'^messages/', views.index, name='messages'),
    url(r'^message/(?P<message_id>\w+)/$', views.view_message, name='view_message'),

]
