from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<login>[a-zA-Z0-9_-]{3,30})/', views.index, name='index'),
]
