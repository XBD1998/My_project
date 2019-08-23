from django.conf.urls import url
from . import views
urlpatterns = [
        url(r'^issue/$', views.Publish.as_view(), name='issue'),
        url(r'^publish/$', views.test, name="publish")
        # url(r'^publish', views.)
        # url(r'^delGoods', 'delGoods'),
        # url(r'^saleHis', 'saleHis'),
        # url(r'message', 'message'),
]
