from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.index, name='login'),
    url(r'^login/$', views.login, name='login'),
    url(r'^regist/$', views.regist, name='regist'),
    url(r'^index/$', views.index, name='index'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^simple$', views.simple, name='simple'),
]
