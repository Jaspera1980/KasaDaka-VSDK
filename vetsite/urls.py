#from django.conf.urls import url

from django.urls import path
from . import views

urlpatterns = [
    path('', views.call_session, name='call_session'),
]