from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^list/(?P<language>.*)/$', views.index, name='index'),
    url(r'^sort/(?P<language>.*)/$', views.sort_it, name='sort_it'),
    url(r'^search/$', views.search, name='search'),

]
