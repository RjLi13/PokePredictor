__author__ = 'ruijing'

"""Urls are how views are called. By visiting an url which is matched by regex, you call the view function
associated with it
"""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^query/$', views.query, name='query'),
]