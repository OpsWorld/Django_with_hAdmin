# -*- coding:UTF-8 -*-
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
"""hAdmin URL Configuration

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
from hAdmin import settings
from django.views.generic.base import TemplateView

urltemplates = [
    url(r'^indexv1', TemplateView.as_view(template_name = 'index_v1.html'), name = 'index_v1'),
    url(r'^projects', TemplateView.as_view(template_name='projects.html'), name='projects'),

    # html可直接通过路径获取静态文本
    # 如果不用这个，可以：
    #       setting里设置  django.contrib.staticfiles
    #       模板头部添加 {% load staticfiles %} 也可以带html中 {% static 'path' %}访问
    url(r'^static(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATICFILES_DIRS})
]

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name = 'index.html'), name = 'root'),
    url(r'^admin/', include(admin.site.urls)),
]


urlpatterns += urltemplates
urlpatterns += staticfiles_urlpatterns()