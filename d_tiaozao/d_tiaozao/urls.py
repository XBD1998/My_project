"""d_tiaozao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^base/$', views.base),
    url(r'^index/$', views.index),
    url(r'^goods_list/$', views.goods_list),
    url(r'^buy_history/$', views.buy_hostory),
    url(r'^goods_detail/$', views.goods_detail),
    url(r'^sale_history/$', views.sale_history),
    url(r'^user_issue/$', views.user_issue),
    url(r'^user_register/$', views.user_register),
    url(r'^login/$', views.login)
]
