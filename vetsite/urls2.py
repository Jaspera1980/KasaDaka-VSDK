#from django.conf.urls import url

from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.chart, name='demo'),
    #path('', views.chart, name='chart'),
]