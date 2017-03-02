# coding:utf-8

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.login, name='login'),              # 登陆
    url(r'^login/$', views.login, name='loginpage'),  # 登陆
    url(r'^logout/$', views.logout, name='logout'),  # 登出
    url(r'^senan/$', views.senan, name='mainsys'),  # 系统主界面
    url(r'^importbasicdata/$', views.importBasicData, name='importBasicData'),  # 基础信息
    url(r'^basicdataview/$', views.basicdataview, name='basicdataview'),        # 基础信息修改
    url(r'^assess/$', views.assess, name='assess'),   # 方案评价
    url(r'^devdebug/$', views.devdebug, name='devdebug'),   # 开发测试
    url(r'^test/$', views.test, name='test'),   # 开发测试
]