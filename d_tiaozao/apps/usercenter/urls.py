from django.conf.urls import url
from . import views

urlpatterns = [
        #个人资料
        url(r'^profile/$', views.test, name='profile'),
        #修改密码
        url(r'^change_passwd/$', views.test, name='change_passwd'),
        #我的回答
        url(r'^answer/$', views.test, name='answer'),
        #我的收藏
        url(r'^collect/$', views.test, name='collect'),
        #接收的消息
        url(r'^message/$', views.Message, name='message')
    ]