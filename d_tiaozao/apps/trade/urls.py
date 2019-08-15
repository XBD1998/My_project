from django.conf.urls import include, url
from . import views
urlpatterns = [
        url(r'^goods_list', views.goods_list, name='goods_list'),
        url(r'^sale_history', views.sale_history, name='sale_history'),
]
