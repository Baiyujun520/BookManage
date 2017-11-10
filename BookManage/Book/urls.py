from django.conf.urls import url
from Book import views

urlpatterns = [
    url(r'^(\w+)/(\w+)/$', views.index),
]