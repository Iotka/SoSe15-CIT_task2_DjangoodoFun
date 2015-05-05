"""todo_project URL Configuration

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

# first input

from django.conf.urls import patterns, include, url
from django.contrib import admin
from TodoLib import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'todo_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'), 
   # url(r'^add/$', views.add, name='add'), 
    url(r'^bearbeiten/$', views.bearbeiten, name='bearbeiten'), 
    url(r'^impressum/$', views.impressum, name='impressum'), 
    url(r'^howto/$', views.howto, name='howto'), 
	url(r'^add/$', views.TaskCreate.as_view(),name='task_add'),
	url(r'^(?P<pk>[0-9]+)$', views.TaskUpdate.as_view(),name='update_add'),
	#TODO:implement delete view /  url(r'^delete/(?P<pk>[0-9]+)/$', views.TaskDelete.as_view(),name='update_delete'),
)

