from django.conf.urls import url
from Book import views

urlpatterns = [
    url(r'^(\w+)/(\w+)/$', views.index),
    url(r'^property/$', views.property),
    url(r'^get/$', views.get),
    url(r'^get1/$', views.get1),
    url(r'^get2/$', views.get2),
    url(r'^post/$', views.post),
    url(r'^post1/$', views.post1),
]