from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^register/', include('register.urls', namespace="register")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<product_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^cart/', views.cart, name='cart'),
]
