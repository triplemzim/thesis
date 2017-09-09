from django.conf.urls import url
from django.contrib import admin

from control import views

urlpatterns = [
    url(r'^$', views.Home),
    url(r'^device/(?P<contactNo>[0-9]{11})/(?P<msg>[A-Z])$', views.DeviceCom),
    url(r'^setup$',views.SetupDevice),
    url(r'^email$',views.sendemail),
]