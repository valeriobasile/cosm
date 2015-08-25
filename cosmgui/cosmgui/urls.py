"""cosmgui URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from codegui import views
#from django.contrib.auth.views import logout as auth_logout

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^dashboard$', views.dashboard, name="dashboard"),
    url(r'^accounts/profile/', views.dashboard, name="dashboard"),
    url(r'^$', views.dashboard, name="dashboard"),
    url(r'^login/$', 'django.contrib.auth.views.login',name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^project/(?P<project_id>[0-9]+)$', views.project),
    url(r'^project/(?P<project_id>[0-9]+)/coding$', views.coding, name='coding'),
    url(r'^project/new$', views.new_project),
    url(r'^save/$', views.save),
]
