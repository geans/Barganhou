from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^register/', include('register.urls', namespace="register")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<local_id>[0-9]+)/$', views.local, name='local'),
    url(r'^cart/', views.cart, name='cart'),
]
