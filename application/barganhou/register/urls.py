from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<product_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<product_id>[0-9]+)/price/$', views.detail, name='price'),
    url(r'^(?P<product_id>[0-9]+)/local/$', views.detail, name='local'),
]
