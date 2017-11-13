from django.conf.urls import url
from Book import views

urlpatterns = [
    url(r'^(\w+)/(\w+)/$', views.index),
    url(r'^property/$', views.property),
    url(r'^get/$', views.get),
    url(r'^get1/$', views.get1),
    url(r'^get2/$', views.get2),
    url(r'^post/$', views.post),
    url(r'^fan/$', views.fan),
    url(r'^fanafan /$', views.fan1, name='fan1'),
    url(r'^post1/$', views.post1),
    url(r'^set_session/$', views.set_session),
    url(r'^get_session/$', views.get_session),
    url(r'^add_num/(\w+)/(\w+)/$', views.add_num),
    url(r'^(\w+)/(\w+)/$', views.add),

]
