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
    url(r'^messages/all/', views.view_all_message, name='all_messages'),
    url(r'^messages/', views.index, name='app_messages'),
    url(r'^message/(?P<message_id>\w+)/$', views.view_message, name='view_message'),
    url(r'^is_valid/(?P<message_id>\w+)/$', views.is_valid, name='app_is_valid'),
    url(r'^no_valid/(?P<message_id>\w+)/$', views.no_valid, name='app_no_valid'),
    url(r'^valid/messages/$', views.view_all_valid_message, name='all_valid'),
    url(r'^bad/messages/$', views.view_no_valid_messages, name='all_no_valid'),
]
