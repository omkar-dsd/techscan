from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^list/(?P<language>[a-zA-Z]+)/$', views.index, name='index'),
    url(r'^search/$', views.search, name='search'),

]