__author__ = 'ruijing'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search, name='search'),
    url(r'^query/$', views.query, name='query'),
    url(r'^(?P<search_id>[0-9a-zA-Z]+)/(?P<custom>[0-9a-zA-Z]+)/results/$', views.results, name='results'),
]