from django.conf.urls import include, url
from . import views
urlpatterns = [
        url(r'^issue/$', views.Issue, name='issue'),
        # url(r'^delGoods', 'delGoods'),
        # url(r'^saleHis', 'saleHis'),
        # url(r'message', 'message'),
]
