__author__ = 'fjywan'

from django.conf.urls import url
from . import views

app_name = 'job'

urlpatterns = [
    url(r'^$', views.index, name='index')
]

