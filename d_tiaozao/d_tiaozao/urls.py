from django.conf.urls import url,include
from django.contrib import admin
from app01 import views
from apps.usercenter import views as uc_views
from django.views.static import serve
from . settings import MEDIA_ROOT
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^base/$', uc_views.index),
    url(r'^accounts/', include('apps.accounts.urls', namespace="accounts")),
    url(r'^uc/', include('apps.usercenter.urls', namespace="uc")),
    url(r'^apis/', include('apps.apis.urls',namespace="apis")),
    # url(r'^base/$', views.base),
    url(r'^trade/', include('apps.trade.urls', namespace="trade")),
    url(r'^goodsIssue/', include('apps.goodsIssue.urls', namespace='goodsIssue')),
    #media处理
    url(r'^media/(?P<path>.*)$', serve, {"document_root":MEDIA_ROOT}),
]
